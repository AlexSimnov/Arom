from django import forms
from .models import Product, Planogram


class DateInput(forms.DateInput):
    input_type = 'date'


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('id',
                  'name',
                  'amount',
                  'date_snat',)
        widgets = {
            'date_snat': DateInput(),
        }


class PlanogramForm(forms.ModelForm):
    class Meta:
        model = Planogram
        fields = ('image',
                  'date_add',)
        widgets = {
            'date_add': DateInput(),
        }
