from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import ProductViewSet, get_max, get_min

router = SimpleRouter()
router.register(r'products', ProductViewSet, basename='products')

urlpatterns = [
    path('products/max_price', get_max),
    path('products/min_price', get_min),
]

urlpatterns += router.urls