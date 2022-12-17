from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from .permissions import PermissionsObj
from .serializers import ProductsSerializers, UserSerializers
from .models import Product
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.


class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductsSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, PermissionsObj]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers
