from django.urls import path, re_path

from  .views import (
    XeroFirstLogin,
    XeroGetTokenInfo,
    XeroRequestCompany,
    XeroPutContact,
    XeroTestClass
)


urlpatterns = [
    path('login/', XeroFirstLogin),
    path('passback/', XeroGetTokenInfo),
    path('test_contact/', XeroPutContact),
    path('test/', XeroTestClass),

]