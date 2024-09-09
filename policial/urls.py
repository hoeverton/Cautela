from django.urls import path
from policial.views import PolicialtCreateView, PolicialListView, PolicialUpdateView, PolicialDetailView

urlpatterns = [
    #path('',PolicialListView.as_view(), name='home'),
    path('policial/create/',PolicialtCreateView.as_view(), name='policial_create'),
    path('policial/<int:pk>/update/',PolicialUpdateView.as_view(), name='policial_update'),
    path('policial/<int:pk>/detail/',PolicialDetailView.as_view(), name='policial_detail'),
    path('policial/list/',PolicialListView.as_view(), name='policial_list'),
    
]