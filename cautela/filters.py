import django_filters
from django import forms
from .models import Cautela, Material, Policial

class CautelaFilter(django_filters.FilterSet):
    # Filtro de Data usando um RangeFilter
    data = django_filters.DateFromToRangeFilter(
        field_name='data',
        label='Data (De - Para)',
        widget=django_filters.widgets.RangeWidget(attrs={'type': 'date', 'class': 'form-control'})
    )
    
    # Filtro de Material usando um ModelChoiceFilter para exibir uma lista de opções de materiais
    material = django_filters.ModelChoiceFilter(
        queryset=Material.objects.all(),
        field_name='material',
        label='Material',
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    # Filtro de Solicitante usando um ModelChoiceFilter para exibir uma lista de opções de solicitantes
    solicitante = django_filters.ModelChoiceFilter(
        queryset=Policial.objects.all(),
        field_name='solicitante',
        label='Solicitante',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    class Meta:
        model = Cautela
        fields = ['data', 'material', 'solicitante']
