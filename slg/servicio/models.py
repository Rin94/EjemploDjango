from django.db import models


# Create your models here.
class Servicio(models.Model):
    nombreServicio = models.CharField(max_length=100, blank=False, null=False, verbose_name="servicio")
    imagenServicio = models.ImageField(upload_to='servicios', null=True, blank=True, verbose_name="imgagen")
    descripcionServicio = models.CharField(max_length=1000, blank=True, null=True, verbose_name="descripcionn")

    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'

    def __str__(self):
        return self.nombreServicio
