from django.urls import path
from .views import CategoriaListView, CategoriaCreateView, CategoriaDetailView, CategoriaUpdateView, CategoriaDeleteView

urlpatterns = [
    
    path('categoria/list/',CategoriaListView.as_view(), name='categoria_list'),
    path('categoria/create/',CategoriaCreateView.as_view(), name='categoria_create'),
    path('categoria/<int:pk>/detail',CategoriaDetailView.as_view(), name='categoria_detail'),
    path('categoria/<int:pk>/delete',CategoriaDeleteView.as_view(), name='categoria_delete'),
    path('categoria/<int:pk>/update',CategoriaUpdateView.as_view(), name='categoria_update'),
   
    
] 