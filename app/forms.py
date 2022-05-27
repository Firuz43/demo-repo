from django import forms

from api.models import Item


class ItemForms(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['category', 'subcategory', 'name', 'amount']
