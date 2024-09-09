from django.contrib import admin
from .models import Policial
from .forms import PolicialForm

class PolicialAdmin(admin.ModelAdmin):
    list_display = ('post_grad','nome_completo', 'nome_guerra', 'cpf_oculto', 'email' )
    search_fields = ('nome_completo', 'cpf', 'email')
    form = PolicialForm
    def cpf_oculto(self, obj):
        return f"{obj.cpf[:3]}.{obj.cpf[3:6]}.***-**"
    cpf_oculto.short_description = 'CPF'

    fieldsets = (
        (None, {
            'fields': ('post_grad', 'nome_completo', 'nome_guerra', 'cpf', 'email', 'senha', 'conf_senha')
        }),
    )
admin.site.register(Policial, PolicialAdmin)