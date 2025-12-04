from .models import Product
from .serializers import ProductSerializer

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response 
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from django.db.models import Max, Min
from rest_framework.decorators import api_view

@api_view()
def get_max(request):
    return Response(Product.objects.aggregate(Max('price')))

@api_view()
def get_min(request):
    return Response(Product.objects.aggregate(Min('price')))


class ProductViewSet(ModelViewSet):
    filterset_fields = ['is_active']
    ordering_fields = ['price']
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    
    serializer_class = ProductSerializer
    queryset = Product.objects.order_by("-updated_at")
    
    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()