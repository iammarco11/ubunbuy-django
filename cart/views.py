from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from cart.models import Product
from django.template import loader
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
    model = Product
    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
        
       return context
