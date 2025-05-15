from django.shortcuts import render, redirect, get_object_or_404
from .models import Deudor, Pedido
from .forms import DeudorForm, PedidoForm
from django.db.models import Sum
from django.utils.html import escape


def lista_deudores(request):
    query = request.GET.get('q', '')
    deudores = Deudor.objects.all()

    if query:
        deudores = deudores.filter(nombre__icontains=query)

    balance_total = deudores.aggregate(Sum('balance'))['balance__sum'] or 0

    return render(request, 'deudores/lista.html', {
        'deudores': deudores,
        'balance_total': balance_total,
        'query': query
    })

def crear_deudor(request):
    form = DeudorForm(request.POST or None)
    if request.method == 'POST':
        print("Datos recibidos:", request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_deudores')
        else:
            print("Errores:", form.errors)
    return render(request, 'deudores/crear.html', {'form': form})


def editar_deudor(request, pk):
    deudor = get_object_or_404(Deudor, pk=pk)
    form = DeudorForm(request.POST or None, instance=deudor)
    if form.is_valid():
        form.save()
        return redirect('lista_deudores')
    return render(request, 'deudores/editar.html', {'form': form})

def eliminar_deudor(request, pk):
    deudor = get_object_or_404(Deudor, pk=pk)
    deudor.delete()
    return redirect('lista_deudores')

def lista_pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, 'pedidos/lista.html', {'pedidos': pedidos})

def crear_pedido(request):
    form = PedidoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_pedidos')
    return render(request, 'pedidos/crear.html', {'form': form})
