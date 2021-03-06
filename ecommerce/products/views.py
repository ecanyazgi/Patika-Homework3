from rest_framework import viewsets

from core.mixins import DetailedViewSetMixin
from products.filters import ProductFilter
from products.models import Product, Category, Stock, Price
from products.serializers import ProductSerializer, CategorySerializer, \
    ProductDetailedSerializer, StockSerializer, PriceSerializer
from products.managers import ProductQuerySet


class ProductViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    manager_class = ProductQuerySet
    queryset = Product.objects.has_stock().action_detailed_list()
    serializer_class = ProductSerializer
    filterset_class = ProductFilter
    serializer_action_classes = {
        "detailed_list": ProductDetailedSerializer,
        "detailed": ProductDetailedSerializer,
    }


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer


class PriceViewSet(viewsets.ModelViewSet):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer