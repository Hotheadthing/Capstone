from django.urls import path
from .views import ProductListView, CategoryListView, CategoryDetailView, ProductDetailView, ProductCategoryView, UserListView,UserCreateView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
urlpatterns = [
    path('list/', ProductListView.as_view(), name='productlist'),
    path('category/', CategoryListView.as_view(), name='categorylist'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='categorydetail'),
    path('list/<int:pk>/', ProductDetailView.as_view(), name='productdetail'),
    path('category/<int:pk>/products/', ProductCategoryView.as_view(), name='productcategory'),
    path('users/', UserListView.as_view(), name='userlist'),
    path('users/create/', UserCreateView.as_view(), name='usercreate'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]