from tkinter.messagebox import NO
from django.http import JsonResponse
from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from base.serailizers import ProductSerializer

from .models import Product

@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/products/',
        '/api/products/create/',
        
        '/api/products/upload/',
        
        '/api/products/<id>/reviews/',
        
        '/api/products/top/',
        '/api/products/<id>/',
        
        '/api/products/delete/<id>/',
        '/api/products/<update>/<id>/',
    ]
    return Response(routes)

@api_view(['GET'])
def getProducts(request):
    products = Product.objects.all()
    serailizer = ProductSerializer(products, many=True)
    return Response(serailizer.data)
    
@api_view(['GET'])
def getProduct(request, pk):
    product = Product.objects.get(pk=pk)
    serailizer = ProductSerializer(product, many=False)

    return Response(serailizer.data)