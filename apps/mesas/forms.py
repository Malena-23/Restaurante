import django.forms as forms
from .models import MesasEstado, Mesa

class MesasEstadoForm(forms.ModelForm):
    class Meta:
        model = MesasEstado
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre del estado de la mesa'})
        }
        
class MesaForm(forms.ModelForm):
    class Meta:
        model = Mesa
        fields = ['nombre', 'capacidad', 'estado']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre de la mesa'}),
            'capacidad': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la capacidad de la mesa'}),
            'estado': forms.Select(attrs={'class': 'form-control'})
        }