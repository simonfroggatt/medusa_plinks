"""medusa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.views.generic.base import TemplateView

from apps.products.views import product_list_asJson
from apps.dashboard.views import order_stats

urlpatterns = [

    path('products/', include('apps.products.urls')),
    path('dashboard/', include('apps.dashboard.urls')),
    path('sales/', include('apps.sales.urls')),
    path('xero/', include('apps.xero_toolkit.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('json_product_data/', product_list_asJson),
    path('', order_stats),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

