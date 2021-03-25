from datetime import datetime

from cliente.forms import ClienteForm
from cliente.models import Cliente, Entidad
from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.db import transaction
from django.db.models import Q
from django.shortcuts import render


# Create your views here.

def dashboard(request):
    if request.user.is_authenticated:
        return render(request, "home/dashboard.html")
    else:
        return render(request, "home/index.html")


@transaction.atomic
def home(request):
    if request.method == "POST":
        notificacion = True
        cl = Cliente.objects.filter \
            (Q(nombres=request.POST['nombres']),
             Q(apellidoPaterno=request.POST['apellidoPaterno']),
             Q(apellidoMaterno=request.POST['apellidoMaterno']),
             Q(telefono=request.POST['telefono']))
        if not cl.exists():
            cl = crearUsuario(request.POST)
        us = User.objects.filter(is_superuser=True)
        if (enviarMensaje(cl.email, us[0].email, cl) == False):
            raise ValueError('A very specific bad thing happened.')
        formContacto = ClienteForm()
        return render(request, "home/index.html", {"notificacion": notificacion, "miFormulario": formContacto})
    else:
        notificacion = False
        formContacto = ClienteForm()
        return render(request, "home/index.html", {"notificacion": notificacion, "miFormulario": formContacto})


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


def listToString(s):
    # initialize an empty string
    str1 = " "
    # return string
    return (str1.join(s))


@transaction.atomic
def enviarMensaje(emailCliente, emailUsuario, cliente):
    try:
        servicios = []
        for ser in cliente.servicios.all():
            servicios.append(ser.__str__())
        print(servicios)
        subject = str(cliente) + " ha solicitado información"
        message = "El cliente" + str(cliente) + '\n' + \
                  " ha solicitado una cita por el próposito de: " + listToString(servicios) + '\n' + \
                  " Con el número de teléfono: " + str(cliente.telefono) + '\n' + \
                  " Email: " + str(cliente.email)
        print(emailUsuario)
        emailFrom = settings.EMAIL_HOST_USER
        recipient_list = [emailCliente, emailUsuario, emailFrom, "sofialopezgarcia417@gmail.com"]
        send_mail(subject=subject, message=message, from_email=emailFrom, recipient_list=recipient_list,
                  fail_silently=False)
        return True
    except Exception as e:
        print(e)
        return False
