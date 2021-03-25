from cliente.models import Cliente, Servicio
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Event(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    notas = models.TextField(blank=False, null=False)
    asesoriaNueva = models.BooleanField(default=False, blank=True)
    start_time = models.DateTimeField(blank=False, null=False)
    end_time = models.DateTimeField()
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE, null=True)
    bloqueado = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return self.start_time.strftime("%H:%M") + "-" + self.title + "-" + self.usuario.username

    @property
    def get_html_url(self):
        if self.bloqueado == False:
            t = aslocaltimestr(self.start_time)
            url = reverse('cal:event_edit', args=(self.id,))
            return f'<a href="{url}"> {t+"-"+self.title+"-"+self.usuario.username} </a>'
        else:
            t = aslocaltimestr(self.start_time)
            t2 = aslocaltimestr(self.end_time)
            url = reverse('cal:event_edit', args=(self.id,))
            return f'<a style="color:red;" href="{url}"> {"Horas bloqueadas: "+self.usuario.username+"-"+t+"-"+t2} </a>'


import pytz

local_tz = pytz.timezone('America/Mexico_City')  # use your local timezone name here


# NOTE: pytz.reference.LocalTimezone() would produce wrong result here

## You could use `tzlocal` module to get local timezone on Unix and Win32
# from tzlocal import get_localzone # $ pip install tzlocal

# # get local timezone
# local_tz = get_localzone()

def utc_to_local(utc_dt):
    local_dt = utc_dt.replace(tzinfo=pytz.utc).astimezone(local_tz)
    return local_tz.normalize(local_dt)  # .normalize might be unnecessary


def aslocaltimestr(utc_dt):
    return utc_to_local(utc_dt).strftime('%H:%M')
