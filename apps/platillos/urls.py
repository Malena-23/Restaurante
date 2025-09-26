from django.urls import path
from . import views

app_name = 'platillos'

urlpatterns = [    
    path('categorias/', views.CategoriaListView.as_view(), name='categoria_list'),
    path('categorias/add/', views.CategoriaCreateView.as_view(), name='categoria_create'),
    path('categorias/<int:pk>/edit/', views.CategoriaUpdateView.as_view(), name='categoria_edit'),
    path('categorias/<int:pk>/delete/', views.CategoriaDeleteView.as_view(), name='categoria_delete'),
    path('platillos/', views.PlatilloListView.as_view(), name='platillos_list'),
]