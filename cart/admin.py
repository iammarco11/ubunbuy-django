from django.contrib import admin

from cart.models import Cart, Product

admin.site.register(Product)
admin.site.register(Cart)
