from django.core.validators import MaxValueValidator, MinLengthValidator
from django.db import models
from servicio.models import Servicio


# Create your models here.

class Entidad(models.Model):
    lugar = models.CharField(max_length=50, blank=False, null=False)

    class Meta:
        verbose_name = 'Entidad'
        verbose_name_plural = 'Entidades'
        ordering = ['lugar']

    def __str__(self):
        return self.lugar


class Cliente(models.Model):
    nombres = models.CharField(max_length=50, blank=False, null=False, verbose_name="nombre(s)")
    apellidoPaterno = models.CharField(max_length=50, blank=False, null=False, verbose_name="Apellido paterno")
    apellidoMaterno = models.CharField(max_length=50, blank=False, null=False, verbose_name="Apellido materno")
    nss = models.PositiveIntegerField(validators=[MaxValueValidator(99999999999), MinLengthValidator(11)], blank=True,
                                      null=True, unique=True, verbose_name="Número de seguridad social")
    email = models.EmailField(max_length=100, blank=True, null=True)
    servicios = models.ManyToManyField(Servicio, blank=False)
    fechaNacimiento = models.DateField(blank=False, null=False, verbose_name="Fecha de nacimiento")
    # telefono=models.PositiveIntegerField(validators=[MaxValueValidator(9999999999), MinLengthValidator(10)],blank=False, null=False,  verbose_name="Teléfono")
    telefono = models.CharField(
        max_length=10,
        blank=False,
        null=False,
    )
    lugarNacimiento = models.ForeignKey(Entidad, on_delete=models.CASCADE, verbose_name="Lugar de nacimiento")
    comentariosCliente = models.CharField(max_length=255, blank=True, null=True, verbose_name="Comentarios")

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.nombres + " " + self.apellidoPaterno
