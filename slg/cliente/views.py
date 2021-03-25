from datetime import datetime
from django.core.paginator import Paginator
from django.db import transaction
from django.shortcuts import render
from .filters import ClienteFilter
from .forms import ClienteForm
from .models import Cliente, Entidad


# Create your views here.
@transaction.atomic
def crearUsuario(datos):
    id = int(datos['lugarNacimiento'])
    entidad = Entidad.objects.get(pk=id)
    nombres = datos['nombres']
    apellidoPaterno = datos['apellidoPaterno']
    apellidoMaterno = datos['apellidoMaterno']
    nss = datos['nss']
    email = datos['email']
    servicios = datos['servicios']
    fechaNacimiento = datos['fechaNacimiento']
    fechaNacimiento = datetime.strptime(fechaNacimiento, '%Y-%m-%d')
    telefono = datos['telefono']
    comentariosCliente = datos['comentariosCliente']
    if nss != "":
        cl = Cliente(nombres=nombres, apellidoPaterno=apellidoPaterno, apellidoMaterno=apellidoMaterno,
                     nss=nss, fechaNacimiento=fechaNacimiento, telefono=telefono, email=email,
                     lugarNacimiento=entidad, comentariosCliente=comentariosCliente)
    else:
        cl = Cliente(nombres=nombres, apellidoPaterno=apellidoPaterno, apellidoMaterno=apellidoMaterno,
                     fechaNacimiento=fechaNacimiento, telefono=telefono, email=email,
                     lugarNacimiento=entidad, comentariosCliente=comentariosCliente)

    cl.save()
    cl.servicios.add(servicios)
    return cl


def listarClientes(request):
    eventos = Cliente.objects.all()
    paginator = Paginator(eventos, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    form = ClienteForm()
    if request.method == "GET":
        myFilter = ClienteFilter(request.GET, queryset=eventos)
        eventos = myFilter.qs
        return render(request, 'cliente/listar.html', {'myFilter': myFilter, 'form': ClienteForm, 'page_obj': eventos})

    if request.method == "POST":
        cl = crearUsuario(request.POST)
        myFilter = ClienteFilter()
        return render(request, "cliente/listar.html", {'myFilter': myFilter, 'form': ClienteForm, 'page_obj': page_obj})
