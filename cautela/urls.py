from django.urls import path
from .views import CautelaListView, CautelaCreateView, CautelaDetailView, CautelaUpdateView, CautelaFinishView, CautelaCreateViewStep1, CautelaFilterView, pdf_view
#, CautelaPDFView



urlpatterns = [
    path('cautela/list/',CautelaListView.as_view(), name='cautela_list'),                            
    path('cautela/create/',CautelaCreateView.as_view(), name='cautela_create'),                                          
    path('cautela/<int:pk>/detail/',CautelaDetailView.as_view(), name='cautela_detail'),                                          
    path('cautela/<int:pk>/update/',CautelaUpdateView.as_view(), name='cautela_update'), 
    path('cautela/<int:pk>/finish/',CautelaFinishView.as_view(), name='cautela_finish'), 
    path('cautela/create_step1/',CautelaCreateViewStep1.as_view(), name='cautela_create_step1'),
    path('cautela/filter/',CautelaFilterView.as_view(), name='cautela_filter'),
    path('generate-pdf/', pdf_view, name='generate_pdf'),
   

   
                                            


] 