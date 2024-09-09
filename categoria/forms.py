from django import forms
from .models import Categoria

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['categoria', 'descricao']
        widgets = {
            'categoria': forms.TextInput(attrs={'class': 'form-control'}), # formatar CSS
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        labels = {
            'categoria': 'Categoria',
            'descricao': 'Descrição'
        }
    def clean_categoria(self):
        categoria = self.cleaned_data.get('categoria')
        if Categoria.objects.filter(categoria=categoria).exists():
            raise forms.ValidationError("Já existe uma categoria com esse nome.")
        return categoria    