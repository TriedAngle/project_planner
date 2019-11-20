from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend


class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['id', 'name', 'seller', 'current_price']
    filterset_fields = ['id', 'name', 'seller', 'current_price']

    def get_queryset(self):
        return self.queryset.order_by('id')
