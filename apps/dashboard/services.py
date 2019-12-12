from apps.products.models import OcOrder
import datetime as dt
import pandas as pd


def range_stats(irange):

    date_range = create_date_range(irange)
    date_range = {'start': '2019-06-01', 'end': '2019-06-30'}
    queryset = OcOrder.objects.orders_range(date_range['start'], date_range['end'])
    #queryset = OcOrder.objects.orders_range('2019-06-01', '2019-06-30')
    qs_dict = queryset.values_list("total", "payment_code", "date_added", "direct_website_order")
    stats_data = create_stats(qs_dict, irange, date_range)

    return stats_data


def create_date_range(irange):
    startdate = dt.date.today()
    enddate = startdate + dt.timedelta(days=1)
    if irange == 'D':
        startdate = dt.date.today()
        enddate = startdate
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
    payment_types = ['PP_PRO', 'PAYPAL_PRO', 'PP_STANDARD', 'SAGEPAY', 'COD']
    po_types = ['PROFORMA', 'PO']

    df = pd.DataFrame(list(pd_data_in), columns=["total", "payment_code", "date_added", "direct_website_order"])  ## this will save 50% memory


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

    idx = pd.date_range(date_range['start'], date_range['end'])

    df2 = pd.DataFrame(list(pd_data_in), columns=["total", "payment_code", "date_added", "direct_website_order"])  ## this will save 50% memory
    df2.asfreq('d').index

   # df2.set_index(idx)

    #df3 = df2.resample('D').count()

    print(df2)

    pd.date_range(date_range['start'], date_range['end'], freq='D')
    df2 = df.set_index('date_added').groupby(['direct_website_order', 'payment_code']).sum()
   # df.set_index('date_added')
   # all_days = pd.date_range(df.index.min(), df.index.max(), freq='D')

    #dtg = df.set_index('date_added').groupby(
    #    ['direct_website_order', 'payment_code', pd.Grouper(freq=irange)]).resample(irange).sum()


    #df.reindex(all_days)

   # print(df2)

    #dtg.reindex(fill_value=0)
    #print(df.loc[all_days])

    return order_stats

