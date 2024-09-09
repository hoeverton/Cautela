from django import forms
from .models import Material

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['categoria', 'titulo', 'patrimonio','descricao']
        widgets = {
            'categoria': forms.Select(attrs={'class': 'form-control'}), # formatar CSS
            'titulo': forms.TextInput(attrs={'class': 'form-control'}), # formatar CSS
            'patrimonio': forms.TextInput(attrs={'class': 'form-control'}), # formatar CSS
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        labels = {
            'categoria': 'Categoria',
            'titulo': 'Título',
            'patrimonio': 'Patrimônio',
            'descricao': 'Descrição'
        }
    def clean_titulo(self):
        titulo = self.cleaned_data.get('titulo')
        # Se necessário, inclua a validação do título aqui
        return titulo
        

    def clean_patrimonio(self):
        patrimonio = self.cleaned_data.get('patrimonio')
        # Verifica se existe algum material com o mesmo patrimônio, excluindo o atual em caso de atualização
        if Material.objects.filter(patrimonio=patrimonio).exclude(id=self.instance.id).exists():
            raise forms.ValidationError("Já existe um material com esse patrimônio.")
        return patrimonio