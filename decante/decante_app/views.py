from django.shortcuts import render, redirect, get_object_or_404
from .models import Deudor, Pedido, Contacto
from .forms import DeudorForm, PedidoForm, ContactoForm
from django.db.models import Sum
from django.utils.html import escape
import vobject
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect



#_______________________CREAR DEUDOR______________________#

def crear_deudor(request):
    if request.method == 'GET' and any(param in request.GET for param in ['nombre', 'telefono', 'direccion']):
        data = {
            'nombre': request.GET.get('nombre', ''),
            'telefono': request.GET.get('telefono', ''),
            'direccion': request.GET.get('direccion', ''),
            'balance': 0
        }
        form = DeudorForm(initial=data)
    else:
        form = DeudorForm(request.POST or None)
        if request.method == 'POST' and form.is_valid():
            form.save()
            return redirect('lista_deudores')

    return render(request, 'deudores/crear.html', {'form': form})


#_______________________VER DEUDOR______________________#
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

#_______________________UPDATE DEUDOR______________________#
def editar_deudor(request, pk):
    deudor = get_object_or_404(Deudor, pk=pk)
    form = DeudorForm(request.POST or None, instance=deudor)
    if form.is_valid():
        form.save()
        return redirect('lista_deudores')
    return render(request, 'deudores/editar.html', {'form': form})

#_______________________DELETE DEUDOR______________________#
def eliminar_deudor(request, pk):
    deudor = get_object_or_404(Deudor, pk=pk)
    deudor.delete()
    return redirect('lista_deudores')





#_______________________VER PEDIDO______________________#
def lista_pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, 'pedidos/lista.html', {'pedidos': pedidos})


#_______________________CREAR PEDIDO______________________#
def crear_pedido(request):
    form = PedidoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_pedidos')
    return render(request, 'pedidos/crear.html', {'form': form})








#_______________________VER CONTACTO______________________#
def lista_contactos(request):
    contactos = Contacto.objects.all()
    return render(request, 'contactos/lista.html', {'contactos': contactos})

#_______________________CREAR CONTACTO______________________#
def crear_contacto(request):
    form = ContactoForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('lista_contactos')
    return render(request, 'contactos/crear.html', {'form': form})

#_______________________UPDATE CONTACTO______________________#
def editar_contacto(request, pk):
    contacto = get_object_or_404(Contacto, pk=pk)
    form = ContactoForm(request.POST or None, instance=contacto)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('lista_contactos')
    return render(request, 'contactos/editar.html', {'form': form})

#_______________________DELETE CONTACTO______________________#
def eliminar_contacto(request, pk):
    contacto = get_object_or_404(Contacto, pk=pk)
    if request.method == 'POST':
        contacto.delete()
        return redirect('lista_contactos')
    return render(request, 'contactos/confirmar_eliminar.html', {'contacto': contacto})

#__________________IMPORTAR CONTACTOS_________________________#

def importar_contactos_vcf(request):
    if request.method == 'POST' and request.FILES.get('archivo'):
        vcf_file = request.FILES['archivo']
        data = vcf_file.read().decode('utf-8', errors='ignore')
        cards_importadas = 0
        fallidas = 0

        bloques = data.split('END:VCARD')
        for bloque in bloques:
            if "BEGIN:VCARD" in bloque:
                bloque_completo = bloque.strip() + "\nEND:VCARD"
                try:
                    vcard = vobject.readOne(bloque_completo)
                    nombre = getattr(vcard, 'fn', None)
                    telefono = getattr(vcard, 'tel', None)
                    empresa = getattr(vcard, 'org', None)
                    comentarios = getattr(vcard, 'note', None)

                    Contacto.objects.create(
                        nombre=nombre.value if nombre else '',
                        telefono=telefono.value if telefono else '',
                        direccion='',
                        empresa=empresa.value[0] if empresa else '',
                        comentarios=comentarios.value if comentarios else ''
                    )
                    cards_importadas += 1
                except Exception as e:
                    fallidas += 1
                    continue

        messages.success(request, f"Contactos importados: {cards_importadas}. Fallidos: {fallidas}")
        return redirect('lista_contactos')

    return render(request, 'contactos/importar_vcf.html')

def seleccionar_contacto_para_deudor(request):
    query = request.GET.get('q', '')
    contactos = Contacto.objects.all()
    if query:
        contactos = contactos.filter(nombre__icontains=query)
    return render(request, 'deudores/seleccionar_contacto.html', {'contactos': contactos})


def cobrar(request):
    deudores = Deudor.objects.filter(balance__gt=F('abonos'))
    mensajes = []

    for d in deudores:
        mensaje = f"""¡Hola {d.nombre}! Para realizar el pago o abono de tus perfumes Decanté, puedes hacerlo a la cuenta a nombre de Eduard Rodolfo P.

Coloca tu nombre en el concepto de pago para identificarlo fácilmente.
¡Gracias por tu preferencia! ✨

Banco: BBVA
CLABE: 012744015125181509

Perfumes: {d.perfumes}
Adeudo: ${d.balance}
Abonos: ${d.abonos}
Restan: ${max(d.balance - d.abonos, 0)}"""
        mensajes.append(mensaje)

    return render(request, 'cobrar.html', {'mensajes': mensajes})

