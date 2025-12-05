from .models import Product
from .serializers import ProductSerializer

from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Max, Min


class ProductViewSet(ModelViewSet):
    filterset_fields = ['is_active']
    ordering_fields = ['price']
    filter_backends = [DjangoFilterBackend]
    
    serializer_class = ProductSerializer
    queryset = Product.objects.order_by("-updated_at")
    
    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()
        
    def get_queryset(self):
        queryset = Product.objects.order_by("-updated_at")
        
        max_price = self.request.query_params.get('max_price')
        if max_price:
            queryset = queryset.filter(price__lte=max_price)
        
        min_price = self.request.query_params.get('min_price')
        if min_price:
            queryset = queryset.filter(price__gte=min_price)
        
        return queryset