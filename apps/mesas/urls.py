from django.urls import path
from . import views

app_name = 'mesas'

urlpatterns = [  
    path('mesas_estado/', views.MesasEstadoListView.as_view(), name='mesas_estado_list'),
    path('mesas_estado/add/', views.MesasEstadoCreateView.as_view(), name='mesas_estado_create'),
    path('mesas_estado/<int:pk>/edit/', views.MesasEstadoUpdateView.as_view(), name='mesas_estado_edit'),
    path('mesas_estado/<int:pk>/delete/', views.MesasEstadoDeleteView.as_view(), name='mesas_estado_delete'),
      
    path('mesas/', views.MesaListView.as_view(), name='mesas_list'),
    path('mesas/add/', views.MesaCreateView.as_view(), name='mesas_create'),
    path('mesas/<int:pk>/edit/', views.MesaUpdateView.as_view(), name='mesas_edit'),
    path('mesas/<int:pk>/delete/', views.MesaDeleteView.as_view(), name='mesas_delete'),
]