"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from ecommerce.router import router
from products.views import ProductViewSet, CategoryViewSet, \
    StockViewSet, PriceViewSet
from baskets.views import BasketViewSet, BasketItemViewSet
from orders.views import BillingAddressViewSet, ShippingAddressViewSet, OrderViewSet, \
    OrderBankAccountViewSet, OrderItemViewSet
from payments.views import BankViewSet,BankAccountViewSet
from customers.views import CountryViewSet,CustomerViewSet, CityViewSet, AddressViewSet

router.register("products", ProductViewSet)
router.register("categories", CategoryViewSet)
router.register("prices", PriceViewSet)
router.register("stocks", StockViewSet)
router.register("baskets", BasketViewSet)
router.register("basket-items", BasketItemViewSet)
router.register("billing-addresses", BillingAddressViewSet)
router.register("shipping-addresses", ShippingAddressViewSet)
router.register("orders", OrderViewSet)
router.register("order-bank-account", OrderBankAccountViewSet)
router.register("order-ıtems", OrderItemViewSet)
router.register("banks", BankViewSet)
router.register("bank-accounts", BankAccountViewSet)
router.register("countries", CountryViewSet)
router.register("cities", CityViewSet)
router.register("customers", CustomerViewSet)
router.register("addresses", AddressViewSet)




urlpatterns = [
    path("api/", include(router.urls)),
    path('admin/', admin.site.urls),
]
