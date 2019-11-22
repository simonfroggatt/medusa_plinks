from django.urls import path, re_path

from  .views import (
    product_list,
    product_grid,
    product_list_view_with_details,
    product_list_asJson,
    product_details_update,
    product_selected_symbols,
    product_list_view_with_details_todo
)


urlpatterns = [
    path('listall/', product_list_view_with_details),
    path('list/', product_list_view_with_details_todo),
    path('grid/', product_grid),
    path('details/<int:prod_id>', product_selected_symbols),
    path('json_product_data/', product_list_asJson)

]