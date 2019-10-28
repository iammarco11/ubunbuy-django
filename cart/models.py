from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, unique=True)
    image = models.FileField(null=True, blank=True)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Cart(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='cart_item')
    quantity = models.FloatField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.name + str(self.quantity)
        
class Login(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pic = models.ImageField(null = True, upload_to = 'media')
    email = models.EmailField(blank=True)
    def __str__(self):
        return self.user.username