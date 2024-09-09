from django.urls import path
from .views import MaterialListView, MaterialCreateView, MaterialDetailView, MaterialUpdateView, MaterialDeleteView


urlpatterns = [
    
    path('material/list/',MaterialListView.as_view(), name='material_list'),
    path('material/create/',MaterialCreateView.as_view(), name='material_create'),
    path('material/<int:pk>/detail/',MaterialDetailView.as_view(), name='material_detail'),
    path('material/<int:pk>/update/',MaterialUpdateView.as_view(), name='material_update'),
    path('material/<int:pk>/delete/',MaterialDeleteView.as_view(), name='material_delete'),
    
] 


    
    