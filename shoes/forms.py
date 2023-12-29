from django.forms import ModelForm
from decimal import Decimal
from django import forms
from .models import Marca,Tenis
from carts.models import Pedido

class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'})
        }

class TenisForm(forms.ModelForm):
    class Meta:
        model = Tenis
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'marca': forms.Select(attrs={'class': 'form-select'}),
            'valor': forms.TextInput(attrs={'class': 'form-control money'}),
            'imagem': forms.FileInput(attrs={'class': 'form-control'}),
        }

        def clean_valor(self):
            valor = self.cleaned_data["valor"]
            return Decimal(valor.replace(",", "."))

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ('status'),
        widgets = {
            'status': forms.Select(attrs={'class': 'form-select'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        