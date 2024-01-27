from django.shortcuts import render
from products.producer import publish
from products.serializers import ProductSerializer
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response 
from .models import Products,User
import random
# Create your views here.


class ProductViewSet(viewsets.ViewSet):
    def list(self, request):  # /api/products :->get
        products = Products.objects.all()
        serializer = ProductSerializer(products, many=True)
        publish()
        return Response(serializer.data, status=status.HTTP_200_OK)

        
    def create(self,request):#/api/products    :->post
        serializer = ProductSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save() 
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    
    
    def retrieve(self,request,pk=None):#/api/products/<str:id>    :->get
        product = Products.objects.get(id=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    
    def update(self,request,pk=None):#/api/products/<str:id>    :->get
        product = Products.objects.get(id=pk)
        serializer = ProductSerializer(instance=product, data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save() 
        return Response(serializer.data)
    
        
    
    def destroy(self,request,pk=None):#/api/products/<str:id>    :->get
        product = Products.objects.get(id=pk)
        product.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    
    
class UserAPIView(APIView):
    def get(self, _):
        user = User.objects.all()
        user = random.choice(user)
        return Response({
            'id': user.id
        })
        