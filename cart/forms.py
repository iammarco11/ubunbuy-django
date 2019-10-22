from django import forms
from .models import Settings

class TickForm(forms.Form):
    tick = forms.BooleanField(label = 'ok')
    class Meta:
        model = Settings
        