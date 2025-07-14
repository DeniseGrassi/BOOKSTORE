"""
URL configuration for bookstore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

import debug_toolbar
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse  # <- Adicionado


def home(request):  # <- View simples
    return HttpResponse("Bem-vinda à API da Bookstore!")


urlpatterns = [
    path("", home),  # <- Rota raiz
    path("__debug__", include(debug_toolbar.urls)),
    path("admin/", admin.site.urls),
    path("bookstore/v1/order/", include("order.urls")),
    path("bookstore/v1/product/", include("product.urls")),
    path("bookstore/v2/order/", include("order.urls")),
    path("bookstore/v2/product/", include("product.urls")),
]
