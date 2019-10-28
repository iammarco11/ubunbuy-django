from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from cart.models import Product, Cart, Login
from django.template import loader
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpRequest, Http404
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .forms import CartForm, UserForm
from django.contrib.auth.decorators import login_required

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
class LoginView(TemplateView):
    template_name = 'cart/login.html'
    model = Login 
    @login_required
    def special(request):
        return HttpResponse("You are logged in !")
    @login_required
    def logout(request):
        return HttpResponse("You are logged out")  
    def login(request):
        
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request,user)
                    return HttpResponseRedirect(reverse('product-list'))
                else:
                    return HttpResponse("Your account was inactive.")
            else:
                print("Someone tried to login and failed.")
                print("They used username: {} and password: {}".format(username,password))
                return HttpResponse("Invalid login details given")
        else:
            return render(request, 'cart/login.html', {})
class RegisterView(TemplateView):
    template_name = 'cart/registeration.html'
    model = Login
    
    def register(request):
        
        registered = False
        if request.method == 'POST':
            user_form = UserForm(data=request.POST)
            if user_form.is_valid():
                user = user_form.save()
                user.set_password(user.password)
                user.save()
                
                registered = True
            else:
                return render (request, 'cart/registeration.html',
            {
            'user_form':user_form,
            'registered':registered
            })
            print(user_form.errors)
        else:
            user_form = UserForm()



