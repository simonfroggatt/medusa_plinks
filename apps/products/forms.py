from django import forms
from .models import OcProductDescription, OcProduct, SsanSymbols, SsanProductSymbols


class ProductDetailsForm(forms.ModelForm):
    class Meta:
        model = OcProductDescription
        fields = [
            'name',
            'description',
            'long_description',
            'meta_title',
            'meta_description',
            'meta_keyword'
        ]
        widget = {
            'name': forms.Textarea(attrs={'cols': 80, 'rows': 20}),
            'description': forms.Textarea(),
            'long_description':  forms.Textarea(),

        }


class SsanProductSymbolsForm(forms.ModelForm):
    class Meta:
        model = SsanProductSymbols
        fields = ['product', 'symbol']
