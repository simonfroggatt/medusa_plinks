from django.urls import path, re_path
from rest_framework import routers
from apps.sales import views
from django.conf.urls import url, include

router = routers.SimpleRouter()
router.register(r'orderlist', views.OrdersList)


from .views import (
    xero_list,
    xero_order_list_asJson,
    xero_push_all,
    shipping_dlg,
    send_email,
    create_ship_template,
    xero_push_all_new
)


urlpatterns = [
    url('^api/', include(router.urls)),
    path('orders', views.order_list, name='ordersall'),
    path('xero_list/', xero_list),
    path('xero_push_all/', xero_push_all_new),
    path('json_xero_order_data/', xero_order_list_asJson),
    path('<int:pk>/shipping', shipping_dlg, name='shipping_dialog'),
    path('<int:pk>/sendemail/', send_email),
    path('<int:pk>/shipped_template', create_ship_template, name='shipped_template'),
   # path('listall/', product_list_view_with_details),
   # path('list/', product_list_view_with_details_todo),
   # path('details/<int:prod_id>', product_selected_symbols),
   # path('json_product_data/', product_list_asJson)

]