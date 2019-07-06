from django import forms
from .models import *


class SelectForm(forms.Form):
    models_cars = forms.ModelChoiceField(queryset=Cars.objects.values_list('name', flat=True).distinct(),
                                         to_field_name='name',
                                         label="Модель:",
                                         required=False,
                                         empty_label="Все")
