from django.urls import path, re_path

from  .views import (
    order_stats
)


urlpatterns = [
    path('sales/', order_stats),
]