from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Policial
from .forms import PolicialForm

class PolicialtCreateView(LoginRequiredMixin, CreateView):
    model = Policial
    template_name = 'policial_create.html'
    form_class = PolicialForm
    success_url = reverse_lazy('policial_list')

class PolicialListView(LoginRequiredMixin, ListView):
    model = Policial
    template_name= 'policial_list.html'
    context_object_name = 'policiais'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        nome = self.request.GET.get('nome')

        if nome:
            queryset = queryset.filter(nome_completo__icontains=nome)

        return queryset 

class PolicialUpdateView(LoginRequiredMixin, UpdateView):    
    model = Policial
    template_name = 'policial_update.html'
    form_class = PolicialForm
    success_url = reverse_lazy('policial_list')         

class PolicialDetailView(LoginRequiredMixin, DetailView):
    model = Policial
    template_name = 'policial_detail.html'