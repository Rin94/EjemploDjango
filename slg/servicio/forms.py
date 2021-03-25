from django.forms import ModelForm, Textarea

from .models import Servicio


class ServicioForm(ModelForm):
    class Meta:
        model = Servicio
        fields = ('__all__')
        widgets = {
            'descripcionServicio': Textarea(attrs={'cols': 50, 'rows': 10}),
        }
