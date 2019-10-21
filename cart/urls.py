from django.urls import path, re_path, include

from cart import views

app_name = 'cart'

urlpatterns = [
    path('', views.ProductListView.as_view(), name='product-list'),
    path('product/<slug:slug>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('cart/<slug:slug>/', views.CartView.as_view(), name='cart'),
]
