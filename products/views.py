# -*- coding:utf-8 -*-
from products.models import ProductItem
from products.serializers import ProductItemSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status


class ProductItemList(generics.ListCreateAPIView):
    queryset = ProductItem.objects.all()
    serializer_class = ProductItemSerializer

    def post(self, request, format=None):
        """ShopIn
        save product data in ProductItem model
        and Operation info in ShopIn model"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductItem.objects.all()
    serializer_class = ProductItemSerializer
