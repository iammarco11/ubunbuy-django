from django import forms
from .models import Cart

class TickForm(forms.ModelForm):
    tick = forms.BooleanField(label = 'ok')
    model = Cart

        