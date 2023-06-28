from django import forms
from .models import OcOrder


class OrderForm(forms.ModelForm):
    class Meta:
        model = OcOrder
        fields = '__all__'