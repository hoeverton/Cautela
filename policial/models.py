from django.db import models
from django.contrib.auth.hashers import check_password as check_password_hash
from django.core.validators import MinLengthValidator
from django.contrib.auth.hashers import make_password, check_password as check_password_hash
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from validate_docbr import CPF

def validate_cpf(value):
    cpf = CPF()
    if not cpf.validate(value):
        raise ValidationError(_('CPF inválido.'))

class Policial(models.Model):
    senha = models.CharField(
        max_length=128, 
        validators=[MinLengthValidator(8)], 
        help_text="Senha deve ter pelo menos 8 caracteres."
    )
    POSTO_GRADUACAO_CHOICES = [
        ('SD', 'Soldado'),
        ('CB', 'Cabo'),
        ('3SGT', '3º Sargento'),
        ('2SGT', '2º Sargento'),
        ('1SGT', '1º Sargento'),
        ('ST', 'Subtenente'),
        ('ASP', 'Aspirante'),
        ('TEN', 'Tenente'),
        ('CAP', 'Capitão'),
        ('MAJ', 'Major'),
        ('TC', 'Tenente-Coronel'),
        ('CEL', 'Coronel'),
    ]
    post_grad = models.CharField(
        max_length=5,
        choices=POSTO_GRADUACAO_CHOICES,
        default='SD',
    )
    nome_completo = models.CharField(max_length=255)
    nome_guerra = models.CharField(max_length=200)
    cpf = models.CharField(
        max_length=11, 
        unique=True, 
        validators=[validate_cpf],
        help_text='Digite um CPF válido.'
    )
    email = models.EmailField(unique=True)
    senha = models.CharField(
        max_length=128, 
        validators=[MinLengthValidator(8)], 
        help_text="Senha deve ter pelo menos 8 caracteres."
    )
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # Criptografa a senha antes de salvar
        if not self.pk:  # Verifica se o objeto é novo
            self.senha = make_password(self.senha)
        super(Policial, self).save(*args, **kwargs) 

    def cpf_oculto(self):
        return f"***.{self.cpf[3:6]}.{self.cpf[6:9]}.**"    

    def __str__(self):
        return f"{self.post_grad} - {self.nome_guerra}"

    def save(self, *args, **kwargs):
        # Criptografa a senha antes de salvar, se ela não estiver criptografada
        if not self.senha.startswith('pbkdf2_'):  # Verifica se a senha já está criptografada
            self.senha = make_password(self.senha)
        super(Policial, self).save(*args, **kwargs) 

    def check_password(self, password):
        print("$$$$$$$$$$$")
        print(password)
        try:
            return check_password(password, self.senha)  # Correção: chamada correta
        except Exception as e:
            raise ValidationError("Ocorreu um erro ao verificar a senha.")
   

    class Meta:
        ordering = ['post_grad']
