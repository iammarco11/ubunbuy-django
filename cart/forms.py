from django import forms
from .models import Cart

class CartForm(forms.ModelForm):
    #tick = forms.BooleanField(label = 'ok')
    class Meta:
        model = Cart
        fields = ['product','quantity']
        widgets = {
            'product':forms.HiddenInput(),
        }

        