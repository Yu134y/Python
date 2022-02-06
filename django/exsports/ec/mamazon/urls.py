from django.urls import path
from mamazon import views

app_name = 'mamazon'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('products/', views.ProductListView.as_view(), name='product-list'),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
]