from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404
from django.db import connection
from django.http import HttpResponse
from datetime import datetime
import json
from apps.xero_toolkit import xeroobjects, xeromanager

from rest_framework import viewsets, generics
from rest_framework.response import Response

from apps.sales.models import OcOrder, SsanTempShipping
from apps.sales.serializers import OrdersSerializer
from apps.sales.forms import OrderForm
from django.template.loader import render_to_string

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse_lazy

from django.core.mail import send_mail
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Create your views here.

class OrdersList(viewsets.ModelViewSet):
    queryset = OcOrder.objects.all().order_by('-order_id')
    serializer_class = OrdersSerializer


def order_list(request):
    template_name = 'order_list.html'
    content = {'content_class': 'ecommerce'}
    return render(request, template_name, content)

def xero_list(request):
    template_name = 'xero_list.html'
    content = {'content_class': 'ecommerce'}
    return render(request, template_name, content)


def xero_order_list_asJson(request):
    datavalue = request.GET.get('list_type')

    sql_string = "SELECT safetysigns_opencart_core.oc_order.order_id,safetysigns_opencart_core.oc_order.date_added," \
                 "safetysigns_opencart_core.oc_order.company,safetysigns_opencart_core.oc_order.firstname," \
                 "safetysigns_opencart_core.oc_order.lastname,safetysigns_opencart_core.oc_order_status.`name`," \
                 "safetysigns_opencart_core.oc_order.total " \
                 "FROM safetysigns_opencart_core.oc_order " \
                 "JOIN safetysigns_opencart_core.oc_order_status ON " \
                 "safetysigns_opencart_core.oc_order.order_status_id=safetysigns_opencart_core.oc_order_status.order_status_id " \
                 "JOIN safetysigns_opencart_core.ssan_payment_status ON " \
                 "safetysigns_opencart_core.oc_order.payment_status_id=safetysigns_opencart_core.ssan_payment_status.id " \
                 "WHERE ((safetysigns_opencart_core.oc_order.xero_invoiceid IS NULL) OR " \
                 "(safetysigns_opencart_core.oc_order.xero_invoiceid='')) AND " \
                 "safetysigns_opencart_core.oc_order.payment_status_id IN (2,3,4) AND " \
                 "safetysigns_opencart_core.oc_order.order_id> 40000"

    with connection.cursor() as cursor:
        cursor.execute(sql_string)
        rows = cursor.fetchall()
        missing_orders_all = json.dumps({"order_data": list(rows)},default=str)
        # data = {'test_data': test_all }
        return HttpResponse(missing_orders_all, content_type='application/json')


def xero_push_all(request):
    limit = 1
    template_name = 'xero_list.html'
    content = {'content_class': 'ecommerce'}
    xero_auth = xeromanager.XeroAuthManager()

    sql_order_details = "SELECT safetysigns_opencart_core.oc_order.*,safetysigns_opencart_core.oc_customer.xero_id " \
                        "FROM safetysigns_opencart_core.oc_order JOIN safetysigns_opencart_core.oc_customer ON " \
                        "safetysigns_opencart_core.oc_order.customer_id=safetysigns_opencart_core.oc_customer.customer_id " \
                        "WHERE ((safetysigns_opencart_core.oc_order.xero_invoiceid IS NULL) OR " \
                        "(safetysigns_opencart_core.oc_order.xero_invoiceid='')) AND " \
                        "safetysigns_opencart_core.oc_order.payment_status_id IN (2,3,4) AND " \
                        "safetysigns_opencart_core.oc_order.order_id> 40000 LIMIT 50"

    with connection.cursor() as cursor:
        cursor.execute(sql_order_details)
        desc = cursor.description
        while True:
            row = cursor.fetchone()
            if row is None:
                break
            row_dict = dict(zip([col[0] for col in desc], row))
            print(row_dict)

            if not row_dict['xero_id']:
                newcontact = xeroobjects.XeroContact()
                customer_details = xero_get_customer_details(row_dict['customer_id'])
                newcontact.create_contact(customer_details)
                customer_addresses = xero_get_customer_addresses(row_dict['customer_id'])
                newcontact.add_address(customer_addresses)
                xero_customer_id = newcontact.save_contact(xero_auth)
                if xero_customer_id is not None:
                    xero_save_customerid(row_dict['customer_id'],xero_customer_id)
                else:
                    last_error = xero_auth.get_error()
                    content['xero_error'] = last_error

            else:
                xero_customer_id = row_dict['xero_id']

            if xero_customer_id is not None:
                newinvoice = xeroobjects.XeroInvoice()
                newinvoice.create_invoice(row_dict, xero_customer_id)
                xero_product_list = xero_get_order_products(row_dict['order_id'])
                newinvoice.add_order_lines(xero_product_list)
                xero_totals = xero_get_order_totals(row_dict['order_id'])
                newinvoice.set_totals(xero_totals['sub_total'], xero_totals['tax'], xero_totals['total'])
                newinvoice.add_shipping(xero_totals['shipping'])
                xero_invoice_id = newinvoice.save_invoice(xero_auth)
                if xero_invoice_id is not None:
                    xero_save_orderid(row_dict['order_id'],xero_customer_id)
                else:
                    last_error = xero_auth.get_error()
                    content['xero_error'] = last_error

    return render(request, template_name, content)


def xero_get_order_products(orderid):
    sql_order_products = 'SELECT oc_order_product.* FROM oc_order_product WHERE oc_order_product.order_id = ' + str(orderid)

    with connection.cursor() as cursor:
        cursor.execute(sql_order_products)
        desc = cursor.description

        order_product_rows = [
            dict(zip([col[0] for col in desc], row))
            for row in cursor.fetchall()
        ]

    return order_product_rows


def xero_get_customer_details(customerid):
    sql_order_customer = "SELECT oc_customer.* FROM oc_customer WHERE oc_customer.customer_id = " + str(customerid)
    with connection.cursor() as cursor:
        cursor.execute(sql_order_customer)
        desc = cursor.description

        order_customer_row = [
            dict(zip([col[0] for col in desc], row))
            for row in cursor.fetchall()
        ]

    return order_customer_row[0]


def xero_get_customer_addresses(customerid):
    sql_address_book = "SELECT oc_address.* FROM oc_address WHERE oc_address.customer_id = " + str(customerid)
    with connection.cursor() as cursor:
        cursor.execute(sql_address_book)
        desc = cursor.description

        customer_address_book = [
            dict(zip([col[0] for col in desc], row))
            for row in cursor.fetchall()
        ]

    return customer_address_book


def xero_get_order_totals(orderid):
    sql_order_totals = "SELECT oc_order_total.code, oc_order_total.value FROM oc_order_total WHERE oc_order_total.order_id = " + str(orderid)
    total_arr = {}
    with connection.cursor() as cursor:
        cursor.execute(sql_order_totals)
        while True:
            row = cursor.fetchone()
            if row is None:
                break
            total_arr[row[0]] = row[1]
    return total_arr

def xero_save_customerid(customer_id, xero_id):
    sql_order_totals = "UPDATE oc_customer SET oc_customer.xero_id = '" + xero_id+ "' WHERE oc_customer.customer_id = " + str(customer_id)
    with connection.cursor() as cursor:
        cursor.execute(sql_order_totals)

def xero_save_orderid(order_id, xero_id):
    sql_order_totals = "UPDATE oc_order SET oc_order.xero_invoiceid = '" + xero_id+ "' WHERE oc_order.order_id = " + str(order_id)
    with connection.cursor() as cursor:
        cursor.execute(sql_order_totals)


def shipping_dlg(request, pk):
    data = dict()
    template = 'shipping_dlg.html'
    order_obj = get_object_or_404(OcOrder, pk=pk)
    shipping_obj = SsanTempShipping.objects.all()

    if request.method == 'POST':
        shipping_method = request.POST.get('shipping_id')
        tracking_code = request.POST.get('tracking_code')
        email_to_in = request.POST.get('email_to')
        send_email_chk = request.POST.get('send_email')
        order_obj.date_shipped = datetime.now()
        order_obj.tracking = tracking_code
        order_obj.shipped_by_company = shipping_method
        order_obj.save()
        if send_email_chk:
            send_res = send_email(request, pk, email_to_in)
        success_url = reverse_lazy('ordersall')
        return HttpResponseRedirect(success_url)


    context = {'shipping_obj': shipping_obj, 'order_id': pk, 'order_obj': order_obj}
    data['html_form'] = render_to_string(template,
                                         context,
                                         request=request
                                         )
    return JsonResponse(data)


def send_email(request, pk, email_to_in):
    subject = 'Order has been shipped'
    #html_content = '<h1>Your order has been shipped</h1>This is <p>the body</p> <b>of</b> the email.'
    from_email = 'sales@safetysignsandnotices.co.uk'
    #recipient_list = ['simonfroggatt76@gmail.com']

    template = 'shipping_template.html'
    context = dict()
    data = dict()
    order_obj = get_object_or_404(OcOrder, order_id=pk)
    shipping_obj = get_object_or_404(SsanTempShipping, code=order_obj.shipped_by_company)
    context['order_ref'] = f'SSAN-{pk}'
    context['tracking_company'] = shipping_obj.name
    context['tracking_ref'] = order_obj.tracking
    context['tracking_url'] = shipping_obj.tracking_url
    context['thumbnail'] = shipping_obj.image

    html_content = render_to_string(template,context, request=request)

    msg = MIMEMultipart('alternative')
    msg['From'] = from_email
    msg['To'] = email_to_in
    msg['Subject'] = subject
    attachment_path = '/path/to/attachment.pdf'

    # Create the HTML MIMEText object
    html_part = MIMEText(html_content, 'html')

    # Attach the HTML part to the MIMEMultipart message
    msg.attach(html_part)

   # with open(attachment_path, 'rb') as file:
   #     attachment = MIMEApplication(file.read(), Name='attachment.pdf')
   #     attachment['Content-Disposition'] = f'attachment; filename="{attachment_path}"'
   #     msg.attach(attachment)

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('sales@safetysignsandnotices.co.uk', 'ksnypkoumutsaqbi')
        server.sendmail(from_email, email_to_in, msg.as_string())
        server.quit()
        # Email sent successfully
        return_message = 'Email sent successfully!'
        bl_sent = True
        # Additional code or response as per your application's requirements
    except smtplib.SMTPException as e:
        # Failed to send email
        error_mereturn_messagessage = f'Error: {str(e)}'
        bl_sent = False

    data = {'sent': bl_sent, 'message':return_message}
    return data



def get_shipping_email(request, order_id):
    template = 'shipping_template.html'
    context = dict()
    data = dict()
    order_obj = get_object_or_404(OcOrder, order_id=order_id)
    shipping_obj = get_object_or_404(SsanTempShipping, code=order_obj.shipped_by_company)
    context['order_ref'] = f'SSAN-{order_id}'
    context['tracking_company'] = shipping_obj.name
    context['tracking_ref'] = order_obj.tracking
    context['tracking_url'] = shipping_obj.tracking_url

    #data['html_email'] = render_to_string(template, context, request=request)
    #return JsonResponse(data)

    return render(request, template, context)

   # data['html_email']
   # render_to_string(template, context, request=request)
   # return JsonResponse(data)


def create_ship_template(request, pk):
    template = 'shipping_template.html'
    context = dict()
    data = dict()
    order_obj = get_object_or_404(OcOrder, order_id=pk)
    shipping_obj = get_object_or_404(SsanTempShipping, code=order_obj.shipped_by_company)
    context['order_ref'] = f'SSAN-{pk}'
    context['tracking_company'] = shipping_obj.name
    context['tracking_ref'] = order_obj.tracking
    context['tracking_url'] = shipping_obj.tracking_url
    context['thumbnail'] = shipping_obj.image

    #data['html_email']  = render_to_string(template,context, request=request)
    #return JsonResponse(data)
    return render(request, template,context)


