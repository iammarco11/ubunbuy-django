from django import forms
from .models import Cart ,Login, Product


class CartForm(forms.ModelForm):
    quantity = forms.IntegerField(min_value=1)
    class Meta:
        model = Cart
        fields = ['product','quantity']
        widgets = {
            'product':forms.HiddenInput(),
            
        }
class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())
    class Meta:
        model = Login
        fields = ('user','password','email','pic')        
