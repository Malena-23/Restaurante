import django.forms as forms
from .models import MesasEstado, Mesa, Orden

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
        
class OrdenForm(forms.ModelForm):
    class Meta:
        model = Orden
        fields = ['mesa', 'empleado']
        widgets = {
            'mesa': forms.Select(attrs={'class': 'form-control'}),
            'empleado': forms.HiddenInput(attrs={'class': 'form-control'})
        }

    def save(self, commit=True):
        orden = super().save(commit=False)
        if commit:
            orden.estatus = 'pendiente' 
            orden.empleado = self.initial['empleado']
            orden.save()
        return orden