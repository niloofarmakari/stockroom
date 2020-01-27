from django.forms import ModelForm
from . import models


class ProductForm(ModelForm):
    class Meta:
        model = models.Product
        fields = ['name', 'product_info']


class PersonForm(ModelForm):
    class Meta:
        model = models.Person
        fields = ['name', 'phone', 'address']
