from django import forms

from .models import OrderModel


class OrderForm(forms.ModelForm):
    class Meta:
        model = OrderModel
        fields = ['service', 'name', 'phone', 'mail', 'comments', 'photo_file', 'document_file']