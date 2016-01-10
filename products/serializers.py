# -*- coding:utf-8 -*-
from rest_framework import serializers
from products.models import ProductItem


class ProductItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductItem
