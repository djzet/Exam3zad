from .models import Product
from rest_framework import serializers
from django.contrib.auth.models import User


class ProductsSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class UserSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
