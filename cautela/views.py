
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.db.models import Q
from .models import Cautela
from .forms import CautelaForm, CautelaFormStep, CautelaFormfinish
from .filters import CautelaFilter
from xhtml2pdf import pisa
from io import BytesIO




class CautelaListView(LoginRequiredMixin, ListView):
    model = Cautela
    template_name = 'cautela_list.html'
    context_object_name = 'cautelas'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        material = self.request.GET.get('material')

        if material:
            queryset = queryset.filter(
                Q(material__titulo__icontains=material) |
                Q(material__patrimonio__icontains=material)
            )
        
        # Adicione a ordenação aqui
        queryset = queryset.order_by('status')  # Ou outro campo relevante

        return queryset
class CautelaCreateView(LoginRequiredMixin, CreateView):
    model = Cautela
    template_name = 'cautela_create.html'
    form_class = CautelaForm
    success_url = reverse_lazy('cautela_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['policias'] = Policial.objects.all()  # Passa todos os policiais para o template
        return context

class CautelaDetailView(LoginRequiredMixin, DetailView):
    model = Cautela
    template_name = 'cautela_detail.html' 

class CautelaUpdateView(LoginRequiredMixin, UpdateView):    
    model = Cautela
    template_name = 'cautela_update.html'
    form_class = CautelaFormStep
    success_url = reverse_lazy('cautela_list')   

class CautelaFinishView(LoginRequiredMixin, UpdateView):    
    model = Cautela
    template_name = 'cautela_finish.html'
    form_class = CautelaForm
    success_url = reverse_lazy('cautela_list') 

class CautelaCreateViewStep1(LoginRequiredMixin, CreateView):
    model = Cautela
    template_name = 'step1.html'
    form_class = CautelaFormStep
    success_url = reverse_lazy('cautela_list')

class CautelaFinishView(LoginRequiredMixin, UpdateView):
    model = Cautela
    template_name = 'step2.html'
    form_class = CautelaFormfinish
    success_url = reverse_lazy('cautela_list')

class CautelaFilterView(LoginRequiredMixin, ListView):
    model = Cautela
    template_name = 'filter.html'  # Seu template HTML
    context_object_name = 'cautelas'
    paginate_by = 10  # Paginação, 10 resultados por página

    def get_queryset(self):
        queryset = Cautela.objects.all().order_by('data')
        # Aplica os filtros ao queryset
        self.filterset = CautelaFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Adiciona o filterset ao contexto para renderizar o formulário
        context['filterset'] = self.filterset
        return context

def render_to_pdf(template_src, context_dict={}):
    template = render_to_string(template_src, context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(template.encode("UTF-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

def pdf_view(request):
    # Aplica os filtros do request à consulta
    filterset = CautelaFilter(request.GET, queryset=Cautela.objects.all())
    context = {
        'cautelas': filterset.qs  # Passa os resultados filtrados para o contexto
    }
    return render_to_pdf('pdf_template.html', context)

