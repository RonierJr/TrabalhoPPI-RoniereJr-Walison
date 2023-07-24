from django.forms import ModelForm
from django import forms
from .models import Marca,Tenis

class MarcaForm(ModelForm):

    class Meta:
        model = Marca
        fields = '__all__'
        widget = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
        }

class TenisForm(ModelForm):

    class Meta:
        model = Tenis
        fields = '__all__'
        widget = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'marca': forms.Select(attrs={'class': 'form-control'}),
            'valor': forms.TextInput(attrs={'class': 'form-control'}),
            'imagem': forms.FileInput(attrs={'class': 'form-control'}),  
        }