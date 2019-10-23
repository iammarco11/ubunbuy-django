from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from cart.models import Product, Cart
from django.template import loader
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpRequest
from .forms import TickForm
class ProductDetailView(DetailView):
    model = Product


    template_name = 'cart/product-detail.html'
    
	

    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
        
       return context

class ProductListView(ListView):
    model = Product
    template_name = 'cart/product-list.html'
    
class CartView(ListView):
    template_name = 'cart/cart.html'
    model = Cart
    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
        
       return context
