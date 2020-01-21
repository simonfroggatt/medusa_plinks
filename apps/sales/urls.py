from django.urls import path, re_path

from .views import (
    xero_list,
    xero_order_list_asJson,
    xero_push_all
)


urlpatterns = [
    path('xero_list/', xero_list),
    path('xero_push_all/', xero_push_all),
    path('json_xero_order_data/', xero_order_list_asJson)
   # path('listall/', product_list_view_with_details),
   # path('list/', product_list_view_with_details_todo),
   # path('details/<int:prod_id>', product_selected_symbols),
   # path('json_product_data/', product_list_asJson)

]