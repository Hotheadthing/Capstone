from rest_framework.serializers import ModelSerializer
from .models import Product,Category,User
from django.contrib.auth.hashers import make_password

class CategoryListSerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = ("id", "cat_name",)

class ProductListSerializer(ModelSerializer):
    category = CategoryListSerializer()
    class Meta:
        model = Product
        fields = ("id","prod_name","description","image","category","price",)

class ProductListSerializerpost(ModelSerializer):
    class Meta:
        model = Product
        fields = ("id","prod_name","description","image","category","price",)

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("id","username","email","password",)

class UserSerializerpost(ModelSerializer):
    class Meta:
        model = User
        fields = ("id","username","email","password",)

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        user = User.objects.create(**validated_data)

        return user

