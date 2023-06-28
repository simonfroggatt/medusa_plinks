from apps.sales.models import OcOrder
import datetime as dt
import pandas as pd


def range_stats(irange):

    date_range = create_date_range(irange)
    #date_range = {'start': '2019-06-01', 'end': '2019-06-30'}
    queryset = OcOrder.objects.orders_range(date_range['start'], date_range['end'])
    #queryset = OcOrder.objects.orders_range('2019-06-01', '2019-06-30')
    qs_dict = queryset.values_list("total", "payment_code", "date_added", "direct_website_order")
    stats_data = create_stats(qs_dict, irange, date_range)
    chart_data = create_chart_data(qs_dict, irange, date_range)
    return {'stats': stats_data, 'chart': chart_data}


def create_date_range(irange):
    startdate = dt.date.today()
    enddate = startdate + dt.timedelta(days=1)
    if irange == 'D':
        startdate = dt.date.today()
        enddate = startdate + dt.timedelta(days=1)
    elif irange == 'W':
        today = dt.date.today()
        startdate = today - dt.timedelta(days=today.weekday())
        enddate = startdate + dt.timedelta(days=6)
    elif irange == 'M':
        today = dt.date.today()
        startdate = today.replace(day=1)
        if startdate.month == 12:  # December
            enddate = dt.date(startdate.year, startdate.month, 31)
        else:
            enddate = dt.date(startdate.year, startdate.month + 1, 1) - dt.timedelta(days=1)

    return {'start': startdate, 'end': enddate}


def create_stats(pd_data_in, irange, date_range):
    order_stats = {'direct': {'count': 0, 'value': 0}, 'medusa': {'count': 0, 'value': 0}, 'account': {'count': 0, 'value': 0}, 'total': {'count': 0, 'value': 0}}
    payment_types = ['PP_PRO', 'PAYPAL_PRO', 'PP_STANDARD', 'SAGEPAY', 'COD', 'SAGEPAY_DIRECT', 'PAYPAL', 'STRIPEPRO']
    po_types = ['PROFORMA', 'PO']

    if len(pd_data_in) <= 0:
        return order_stats

    df = pd.DataFrame(list(pd_data_in), columns=["total", "payment_code", "date_added", "direct_website_order"])

    order_stats['total']['count'] = df['total'].count()
    order_stats['total']['value'] = df['total'].sum()
    counts_df = df.groupby(['direct_website_order', 'payment_code']).count()
    totals_df = df.groupby(['direct_website_order', 'payment_code']).sum()

    #get the count of the different order types
    count = counts_df.T.to_dict('index')
    count_values = count.get('total')
    for count_type, count_qty in count_values.items():
        if count_type[1].upper() in payment_types:
            if count_type[0] == 0:
                order_stats['medusa']['count'] += count_qty
            else:
                order_stats['direct']['count'] += count_qty
        elif count_type[1].upper() in po_types:
            order_stats['account']['count'] += count_qty

    #get the value of the different order types
    totals = totals_df.T.to_dict('index')
    total_values = totals.get('total')
    for total_type, total_qty in total_values.items():
        if total_type[1].upper() in payment_types:
            if total_type[0] == 0:
                order_stats['medusa']['value'] += total_qty
            else:
                order_stats['direct']['value'] += total_qty
        elif total_type[1].upper() in po_types:
            order_stats['account']['value'] += total_qty

    return order_stats


def create_weekly_data(pd_data_in, date_range):
    # chart_type_stats = {'direct': {'count': 0, 'value': 0}, 'medusa': {'count': 0, 'value': 0}, 'account': {'count': 0, 'value': 0}, 'total': {'count': 0, 'value': 0}}
    chart_period_stats = {
        'direct': [0, 0, 0, 0, 0, 0, 0],
        'medusa': [0, 0, 0, 0, 0, 0, 0],
        'account': [0, 0, 0, 0, 0, 0, 0],
        'total': [0, 0, 0, 0, 0, 0, 0]
    }

    payment_types = ['PP_PRO', 'PAYPAL_PRO', 'PP_STANDARD', 'SAGEPAY', 'COD', 'SAGEPAY_DIRECT', 'PAYPAL', 'STRIPEPRO']
    po_types = ['PROFORMA', 'PO']

    if len(pd_data_in) <= 0:
        return chart_period_stats

    df = pd.DataFrame(list(pd_data_in), columns=["total", "payment_code", "date_added", "direct_website_order"])
    df['day_of_week'] = df['date_added'].dt.dayofweek
    totals_df = df.groupby(['day_of_week', 'direct_website_order', 'payment_code']).sum()
    totals_df['total'] = totals_df['total'].apply(pd.to_numeric, errors='coerce')

    totals = totals_df.T.to_dict('index')
    total_values = totals.get('total')
    for total_type, total_qty in total_values.items():  # total_type = ['day of week', 'website_direct', 'payment_type']
        dow = total_type[0]
        if total_type[2].upper() in payment_types:
            if total_type[1] == 0:
                chart_period_stats['medusa'][dow] += round(total_qty, 2)
            else:
                chart_period_stats['direct'][dow] += round(total_qty, 2)
        elif total_type[2].upper() in po_types:
            chart_period_stats['account'][dow] += round(total_qty, 2)
        chart_period_stats['total'][dow] += round(total_qty, 2)

    return {'datapoint': chart_period_stats, 'range': date_range}


def create_monthly_data(pd_data_in, date_range):

    chart_period_stats = {}

    if len(pd_data_in) <= 0:
        chart_period_stats[dt.datetime.strftime(date_range['start'], "%Y-%m-%d")] = 0
    else:
        df = pd.DataFrame(list(pd_data_in), columns=["total", "payment_code", "date_added", "direct_website_order"])

        df['date_added'] = df['date_added'].dt.date

        totals_df = df.groupby(['date_added'])[['total']].sum() #need to sum the total column
        totals_df['total'] = totals_df['total'].apply(pd.to_numeric, errors='coerce')

        totals = totals_df.T.to_dict('index')

        total_values = totals.get('total')
        for k, v in total_values.items():
            try:
                chart_period_stats[dt.datetime.strftime(k, "%Y-%m-%d")] = v
            except ValueError:
                chart_period_stats[dt.datetime.strftime(k, "%Y-%m-%d")] = 0

    return {'datapoint': chart_period_stats, 'range': {'start': dt.datetime.strftime(date_range['start'], "%Y-%m-%d"), 'end': dt.datetime.strftime(date_range['end'], "%Y-%m-%d")}}


def create_chart_data(pd_data_in, irange, date_range):
    if irange == 'W':
        return create_weekly_data(pd_data_in, date_range)
    elif irange == 'M':
        return create_monthly_data(pd_data_in, date_range)




