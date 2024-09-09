from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from . import models, forms

class MaterialListView(LoginRequiredMixin, ListView):
    model = models.Material
    template_name= 'material_list.html'
    context_object_name = 'materiais'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        titulo = self.request.GET.get('titulo')

        if titulo:
            queryset = queryset.filter(titulo__icontains=titulo)

        return queryset

class MaterialCreateView(LoginRequiredMixin, CreateView):
    model = models.Material
    template_name = 'material_create.html'
    form_class = forms.MaterialForm
    success_url = reverse_lazy('material_list')

class MaterialDetailView(LoginRequiredMixin, DetailView):
    model = models.Material
    template_name = 'material_detail.html'  

class MaterialUpdateView(LoginRequiredMixin, UpdateView):    
    model = models.Material
    template_name = 'material_update.html'
    form_class = forms.MaterialForm
    success_url = reverse_lazy('material_list')         

class MaterialDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Material
    template_name = 'material_delete.html'
    success_url = reverse_lazy('material_list')