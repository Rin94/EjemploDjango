from django.contrib import admin

from .forms import ClienteForm
# Register your models here.
from .models import Cliente, Entidad


class ClienteAdmin(admin.ModelAdmin):
    form = ClienteForm


class EntidadAdmin(admin.ModelAdmin):
    ordering = ['lugar']


admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Entidad, EntidadAdmin)
