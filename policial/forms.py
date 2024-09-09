from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Policial

class PolicialForm(forms.ModelForm):
    conf_senha = forms.CharField(
        widget=forms.PasswordInput(),
        label="Confirme a Senha"
    )

    class Meta:
        model = Policial
        fields = ['nome_completo', 'nome_guerra', 'cpf', 'email', 'senha', 'post_grad']
        widgets = {
            'nome_completo': forms.TextInput(attrs={'class': 'form-control'}),
            'nome_guerra': forms.TextInput(attrs={'class': 'form-control'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control', 'maxlength': '11'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'senha': forms.PasswordInput(attrs={'class': 'form-control'}),
            'post_grad': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'nome_completo': 'Nome Completo',
            'nome_guerra': 'Nome de Guerra',
            'cpf': 'CPF',
            'email': 'Email',
            'senha': 'Senha',
            'post_grad': 'Posto de Graduação',
        }

    def clean(self):
        cleaned_data = super().clean()
        senha = cleaned_data.get("senha")
        conf_senha = cleaned_data.get("conf_senha")

        if senha and conf_senha and senha != conf_senha:
            self.add_error('conf_senha', "As senhas não correspondem.")
        elif not senha:
            self.add_error('senha', "Este campo é obrigatório.")

        return cleaned_data
