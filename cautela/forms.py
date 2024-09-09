from django import forms
from django_select2.forms import Select2Widget 
from django.core.exceptions import ValidationError
from .models import Cautela, Material, Policial
from django.contrib.auth.hashers import check_password

class CautelaForm(forms.ModelForm):
    
    # Sobrescrevendo o campo material
    material = forms.ModelChoiceField(
        queryset=Material.objects.all(),
        widget=Select2Widget(attrs={'class': 'form-control'}),
        label="Material"
    )
    
    
    class Meta:
        model = Cautela
        fields = ['status','furriel', 'material', 'opcao', 'solicitante',  'entregador', 'recebedor', 'alteracao']
        widgets = {
            #'data': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}), # formatar CSS
            'furriel': forms.Select(attrs={'class': 'form-control'}), # formatar CSS
            'opcao': forms.TextInput(attrs={'class': 'form-control'}), # formatar CSS
            'solicitante': forms.Select(attrs={'class': 'form-control'}), # formatar CSS
            #'data_entrega': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}), # formatar CSS
            'entregador': forms.Select(attrs={'class': 'form-control'}), # formatar CSS
            'recebedor': forms.Select(attrs={'class': 'form-control'}), # formatar CSS
            'alteracao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        labels = {
            #'data': 'Data',
            'furriel': 'Furriel',
            'material': 'Material',
            'opcao': 'Opção',
            'solicitante': 'Solicitante',
            #'data_entrega': 'Data de Entrega',
            'entregador': 'Entregador',
            'recebedor': 'Recebedor',
            'alteracao': 'Alteração'
        }

    def __init__(self, *args, **kwargs):
        super(CautelaForm, self).__init__(*args, **kwargs)
        # Personalizando o texto exibido no dropdown para o campo material
        self.fields['material'].label_from_instance = lambda obj: f"{obj.titulo} - Patrimônio: {obj.patrimonio}"

    

    


def verificar_senha_policial(policial, senha_inserida):
    try:
        # Imprime a senha criptografada armazenada no banco
       # print(f"Senha armazenada no banco (criptografada): {policial.senha}")
        #print(f"Senha inserida: {senha_inserida}")

        # Verifica se a senha inserida corresponde à senha criptografada
        senha_correta = check_password(senha_inserida, policial.senha)

        if senha_correta:
            print("A senha inserida está correta.")
        else:
            print("A senha inserida está incorreta.")

        return senha_correta

    except Exception as e:
        print(f"Erro ao verificar a senha: {e}")
        return False

class CautelaFormStep(forms.ModelForm):
    senha = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="Senha do Solicitante",
        required=True
    )
    # Sobrescrevendo o campo material
    material = forms.ModelChoiceField(
        queryset=Material.objects.all(),
        widget=Select2Widget(attrs={'class': 'form-control'}),
        label="Material"
    )
    
    class Meta:
        model = Cautela
        fields = ['status', 'furriel', 'material', 'opcao', 'solicitante','senha']
        widgets = {
            'furriel': forms.Select(attrs={'class': 'form-control'}), # formatar CSS
            'opcao': forms.TextInput(attrs={'class': 'form-control'}), # formatar CSS
            'solicitante': forms.Select(attrs={'class': 'form-control'}), # formatar CSS
        }
        labels = {
            'furriel': 'Furriel',
            'material': 'Material',
            'opcao': 'Opção',
            'solicitante': 'Solicitante',
            'senha' : 'Senha',
        }

    def __init__(self, *args, **kwargs):
        super(CautelaFormStep, self).__init__(*args, **kwargs)
        # Personalizando o texto exibido no dropdown para o campo material
        self.fields['material'].label_from_instance = lambda obj: f"{obj.titulo} - Patrimônio: {obj.patrimonio}"

    def clean_material(self):
        material = self.cleaned_data['material']
        patrimonio = material.patrimonio

        # Se for uma atualização, ignore a própria cautela
        if self.instance.pk:
            existing_cautela = Cautela.objects.filter(
                material=material,
                status='aberto'
            ).exclude(pk=self.instance.pk)
        else:
            existing_cautela = Cautela.objects.filter(
                material=material,
                status='aberto'
            )

        if existing_cautela.exists():
            raise ValidationError(f"O material com o patrimônio '{patrimonio}' já está em uma cautela 'Em aberto'.")

        return material

    def clean_solicitante(self):
        solicitante = self.cleaned_data.get('solicitante')
        senha_inserida = self.data.get('senha')  

        try:
            # Obtenha a instância do Policial baseado no furriel selecionado
            policial = Policial.objects.get(pk=solicitante.id)
            print('########')
            print(policial.id)

            # Chama a função para verificar a senha
            if not verificar_senha_policial(policial, senha_inserida):
                raise ValidationError("Senha incorreta para o solicitante fornecido.")
        except Policial.DoesNotExist:
            raise ValidationError("O solicitante não existe.")

        return solicitante

class CautelaFormfinish(forms.ModelForm):

    senha = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="Senha do Recebedor",
        required=True
    )    
    
    class Meta:
        model = Cautela
        fields = ['status', 'entregador', 'recebedor', 'alteracao','senha']
        widgets = {
            'entregador': forms.Select(attrs={'class': 'form-control'}), # formatar CSS
            'recebedor': forms.Select(attrs={'class': 'form-control'}), # formatar CSS
            'alteracao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            
        }
        labels = {
            'entregador': 'Entregador',
            'recebedor': 'Recebedor',
            'alteracao': 'Alteração',            
            'senha' : 'Senha do Recebedor',
        }


    def clean_recebedor(self):
        recebedor = self.cleaned_data.get('recebedor')
        senha_inserida = self.data.get('senha')  

        try:
            # Obtenha a instância do Policial baseado no furriel selecionado
            policial = Policial.objects.get(pk=recebedor.id)
            print('########')
            print(policial.id)

            # Chama a função para verificar a senha
            if not verificar_senha_policial(policial, senha_inserida):
                raise ValidationError("Senha incorreta para o recebedor fornecido.")
        except Policial.DoesNotExist:
            raise ValidationError("O recebedor não existe.")

        return recebedor     

    def clean_status(self):
        status = self.cleaned_data.get('status')

        # Regra de negócio: o status deve ser 'fechado' para finalizar
        if status != 'fechado':
            raise ValidationError("A Cautela só pode ser finalizada com o status 'Fechado'.")

        return status    