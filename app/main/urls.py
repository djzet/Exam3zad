from django.urls import path, include
from rest_framework import routers
from .views import ProductsViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r'products', ProductsViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework'))
]
