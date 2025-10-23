from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Count
from apps.mesas.models import Orden
from datetime import datetime

def main_index(request):
  		return render(request, 'main/index.html')

@login_required(login_url='accounts:login')
def index_user(request):
    ordenes_hoy = Orden.objects.filter(estatus='pagada', fecha_hora__date=datetime.today())    

    total_sales = sum(orden.total for orden in ordenes_hoy)
    cantidad_ordenes = ordenes_hoy.count()

    context = {
        'ventas_totales': total_sales,
        'cantidad_ordenes': cantidad_ordenes,
    }
    
    return render(request, 'main/index_user.html', context)


