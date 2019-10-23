from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from cart.models import Product, Cart
from django.template import loader
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpRequest
from django.shortcuts import redirect
from .forms import CartForm
from django.http import Http404
from .models import Cart
class ProductDetailView(DetailView):
    model = Product


    template_name = 'cart/product-detail.html'
    
	

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['form'] = CartForm(initial={'product': self.get_object()})
        return context

    def post(self, request, *args, **kwargs):
        
        form = CartForm(self.request.POST)
        self.object = self.get_object()
        if form.is_valid():
            form.save()
            return redirect('cart:cart')
        context = self.get_context_data(**kwargs)
        context['form'] = form
        return self.render_to_response(context)


class ProductListView(ListView):
    model = Product
    template_name = 'cart/product-list.html'
    
class CartView(ListView):
    template_name = 'cart/cart.html'
    model = Cart
    def post(self, request, *args, **kwargs):
        cart_id = self.request.POST.get('cart_id')
        cart_obj=Cart.objects.filter(id=cart_id).first()
        if cart_obj:
            cart_obj.delete()
            return redirect('cart:cart')
        raise Http404()    
     