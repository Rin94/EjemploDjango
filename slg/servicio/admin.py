from django.contrib import admin

from .forms import ServicioForm
# Register your models here.
from .models import Servicio


# Register your models here.


class ServicioAdmin(admin.ModelAdmin):
    form = ServicioForm


admin.site.register(Servicio, ServicioAdmin)
