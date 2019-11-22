from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.core import serializers
from django.http import HttpResponse
import json
# Create your views here.

from .models import (
    OcProduct,
    OcProductDescription,
    SsanProductSymbols,
    SsanSymbols
)

from .forms import (
    ProductDetailsForm,
    SsanProductSymbolsForm,
)


def product_list(request):
    template_name = 'products_list.html'
    content = {'content_class': 'ecommerce'}
    print(content)
    return render(request, template_name, content)


def product_grid(request):
    template_name = 'products_grid.html'
    content = {'content_class': 'ecommerce'}
    return render(request, template_name)


def product_grid(request, pk):
    template_name = 'product_details.html'
    context = {'pk': pk}
    return render(request, template_name, context)



def product_list_view_with_details(request):
    template_name = 'products_list.html'
    # context = {'product_list': []}
    # sql_string = "SELECT oc_product.product_id, oc_product.model, oc_product_description.`name`, " \
    #              "oc_product_description.description, oc_product.image " \
    #              "FROM oc_product JOIN oc_product_description ON " \
    #              "oc_product.product_id = oc_product_description.product_id"
    # with connection.cursor() as cursor:
    #     cursor.execute(sql_string)
    #     rows = cursor.fetchall()
    #     test_all = json.dumps({"data": list(rows)})
    #     data = {'test_data': test_all, }
    context = {'product_list_type': 'all'}
    return render(request, template_name, context)


def product_list_view_with_details_todo(request):
    template_name = 'products_list.html'
    # context = {'product_list': []}
    # sql_string = "SELECT oc_product.product_id, oc_product.model, oc_product_description.`name`, " \
    #              "oc_product_description.description, oc_product.image " \
    #              "FROM oc_product JOIN oc_product_description ON " \
    #              "oc_product.product_id = oc_product_description.product_id " \
    #              "AND NOT EXISTS (SELECT * FROM ssan_product_symbols WHERE ssan_product_symbols.product_id = oc_product.product_id)"
    # with connection.cursor() as cursor:
    #     cursor.execute(sql_string)
    #     rows = cursor.fetchall()
    #     test_all = json.dumps({"data": list(rows)})
    #     data = {'test_data': test_all, }
    #     data = {}
    context = {'product_list_type': 'todo'}
    return render(request, template_name, context)


def product_list_asJson(request):
    template_name = 'products_list.html'
    context = {'product_list': []}

    datavalue = request.GET.get('list_type')

    if datavalue == 'all' :
        sql_string = "SELECT oc_product.product_id, oc_product.model, oc_product_description.`name`, " \
                 "oc_product_description.description, oc_product.image " \
                 "FROM oc_product JOIN oc_product_description ON " \
                 "oc_product.product_id = oc_product_description.product_id"
    else:
        sql_string = "SELECT oc_product.product_id, oc_product.model, oc_product_description.`name`, " \
                     "oc_product_description.description, oc_product.image " \
                     "FROM oc_product JOIN oc_product_description ON " \
                     "oc_product.product_id = oc_product_description.product_id " \
                      "AND NOT EXISTS (SELECT * FROM ssan_product_symbols WHERE ssan_product_symbols.product_id = oc_product.product_id)"
    with connection.cursor() as cursor:
        cursor.execute(sql_string)
        rows = cursor.fetchall()
        product_all = json.dumps({"product_data": list(rows)})
        # data = {'test_data': test_all }
        return HttpResponse(product_all, content_type='application/json')


def product_details_update(request, prod_id):
    template_name = 'product_details_description.html'
    obj = get_object_or_404(OcProductDescription, pk=prod_id)

    form = ProductDetailsForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {'form_desc': form}
    return render(request, template_name, context)


def product_selected_symbols(request, prod_id):


    template_name = 'product_details_symbols.html'
    prod_obj = get_object_or_404(OcProduct, pk=prod_id)
    prod_name = product_name_from_id(prod_id)
    prod_sym_obj = prod_obj.ssanproductsymbols_set.all()

    if request.method == 'POST':
        symbols_selected = request.POST.getlist("symbols_picked")
        prod_sym_obj.delete()
        for hid in symbols_selected:
            prod_sym_obj.update_or_create(product_id=prod_id, symbol_id=hid)


    all_sym_obj = SsanSymbols.objects.all()

    symbol_id_list_qs = prod_sym_obj.values_list('symbol__id',flat=True)
    current_symbol_list = list(symbol_id_list_qs)

    context = {'prod_data': prod_obj, 'product_symbols': prod_sym_obj, 'all_sym_obj': all_sym_obj, 'prod_name': prod_name, 'current_symbol_list': current_symbol_list}
    return render(request, template_name, context)


def product_name_from_id(prod_id):
    obj = OcProductDescription.objects.get(pk=prod_id)
    return obj.name


#  form = BlogPostModelForm(request.POST or None, request.FILES or None)
#     if form.is_valid():
#         obj = form.save(commit=True)
#         obj.user = request.user
#         obj.save()
#         form = BlogPostModelForm()
#     template_name = 'form.html'
#     context = {'form': form}
#     return render(request, template_name, context)