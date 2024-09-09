from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from . import models,forms


class CategoriaListView(LoginRequiredMixin, ListView):
    model = models.Categoria
    template_name= 'categoria_list.html'
    context_object_name = 'categorias'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        categoria = self.request.GET.get('categoria')

        if categoria:
            queryset = queryset.filter(categoria__icontains=categoria)

        return queryset

        
class CategoriaCreateView(LoginRequiredMixin, CreateView):
    model = models.Categoria
    template_name = 'categoria_create.html'
    form_class = forms.CategoriaForm
    success_url = reverse_lazy('categoria_list')

class CategoriaDetailView(LoginRequiredMixin, DetailView):
    model = models.Categoria
    template_name = 'categoria_detail.html' 

class CategoriaUpdateView(LoginRequiredMixin, UpdateView):    
    model = models.Categoria
    template_name = 'categoria_update.html'
    form_class = forms.CategoriaForm
    success_url = reverse_lazy('categoria_list')  

class CategoriaDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Categoria
    template_name = 'categoria_delete.html'
    success_url = reverse_lazy('categoria_list')

class CategoriaUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Categoria
    template_name = 'categoria_update.html'
    form_class = forms.CategoriaForm
    success_url = reverse_lazy('categoria_list')  


