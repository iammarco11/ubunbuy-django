from django.views.generic import TemplateView
from django.views.generic.list import ListView

from cart.models import Product

class ProductDetailView(TemplateView,ListView):
    model = Product


    template_name = 'cart/product-detail.html'
    
	

    #def get_context_data(self, **kwargs):
     #   context = super().get_context_data(**kwargs)
        
      #  return context



class ProductListView(TemplateView):
    
    template_name = 'cart/product-list.html'

class CartView(TemplateView):
    template_name = 'cart/cart.html'
    
