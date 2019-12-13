from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
import datetime
import pandas as pd
import apps.dashboard.services as sv

from apps.products.models import OcOrder
# Create your views here.

#Daily, weekly, monthly, customrange

def order_stats(request):
    template_name = 'sales.html'
    order_stats_daily = sv.range_stats('D')
    order_stats_weekly = sv.range_stats('W')
    order_stats_monthly = sv.range_stats('M')

    content = {'content_class': 'stats', 'daily_stats': order_stats_daily, 'weekly_stats': order_stats_weekly, 'monthly_stats': order_stats_monthly}
    return render(request, template_name, content)




