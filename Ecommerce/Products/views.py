from django.shortcuts import render
from .models import Product,Category,User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 
from .serializers import ProductListSerializer, CategoryListSerializer, ProductListSerializerpost,UserSerializer,UserSerializerpost
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.
class UserListView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request):
        users = User.objects.all()
        serialize_data = UserSerializer(users, many = True)

        return Response(serialize_data.data,status=status.HTTP_200_OK)


class UserCreateView(APIView):
    def post(self,request):
        serialize_data = UserSerializerpost(data=request.data)

        if serialize_data.is_valid():
            user = serialize_data.save()
            refresh = RefreshToken.for_user(user)
            response_data = {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        else:
            return Response(serialize_data.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductListView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request):
        product = Product.objects.all()
        serialize_data = ProductListSerializer(product, many = True)

        return Response(serialize_data.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        serialize_data = ProductListSerializerpost(data=request.data)

        if serialize_data.is_valid():
            serialize_data.save()
            return Response(serialize_data.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serialize_data.errors, status=status.HTTP_400_BAD_REQUEST)
    

class CategoryListView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request):
        categories = Category.objects.all()
        serializer = CategoryListSerializer(categories,many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer = CategoryListSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request,pk):
        category = Category.objects.filter(id=pk).first()
        if category:
            serializer = CategoryListSerializer(category)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response("No category has been assigned to this primary key", status=status.HTTP_204_NO_CONTENT)


class ProductDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request,pk):
        product = Product.objects.filter(id=pk).first()
        if product:
            serializer = ProductListSerializer(product)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response("No product has been assigned to this primary key", status=status.HTTP_204_NO_CONTENT)

class ProductCategoryView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request,pk):
        category = Category.objects.filter(id=pk).first()
        if category:
            products = Product.objects.filter(category=category)
            serializer = ProductListSerializer(products,many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response("No category has been assigned to this primary key", status=status.HTTP_204_NO_CONTENT)

