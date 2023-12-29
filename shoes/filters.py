import django_filters
from django import forms
from .models import Tenis


class TenisFilter(django_filters.FilterSet):
    nome = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'placeholder': 'Pesquisar'})
    )

    class Meta:
        model = Tenis
        fields = ['nome']
        