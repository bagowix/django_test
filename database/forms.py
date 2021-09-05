from .models import DataBase
from django.forms import ModelForm, TextInput, DateInput, NumberInput, Select


class DataBaseForm(ModelForm):
    class Meta:
        model = DataBase
        fields = ['productName', 'quantity', 'unit', 'price', 'date']

        widgets = {
            "productName": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название товара'
            }),
            "quantity": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Количество товара'
            }),
            "unit": Select(attrs={
                'class': 'form-control',
                'label': 'Единица измерения'
            }),
            "price": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Цена товара'
            }),
            "date": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата последней поставки или отгрузки'
            })
        }
