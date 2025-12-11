from products.models import Product
from rest_framework import serializers
from rest_framework import viewsets


class ProductSerializer(serializers.ModelSerializer):
  class Meta:
    model = Product
    fields = ['id', 'name', 'price', 'category']


class AllProductsViewSet(viewsets.ModelViewSet):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
