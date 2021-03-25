from django import forms
from django.forms import ModelForm, Textarea
from phonenumber_field.formfields import PhoneNumberField
from servicio.models import Servicio

from .models import Cliente


class ClienteForm(ModelForm):
    nombres = \
        forms.CharField(label='Nombre(s)',
                        widget=forms.TextInput(attrs={'placeholder': 'Nombre(s)',
                                                      'class': 'form-control'}))
    apellidoPaterno = forms.CharField(label='Apellido paterno',
                                      widget=forms.TextInput(attrs=
                                                             {'placeholder': 'Apellido paterno',
                                                              'class': 'form-control'}))
    apellidoMaterno = forms.CharField(label='Apellido materno',
                                      widget=forms.TextInput(attrs={'placeholder': 'Apellido materno',
                                                                    'class': 'form-control'}))
    nss = forms.IntegerField(required=False, min_value=1000000000, max_value=99999999999,
                             label='Número de seguridad social',
                             widget=forms.NumberInput(attrs={'placeholder': 'NSS',
                                                             'class': 'form-control'}))
    email = forms.EmailField(label="Correo electrónico", required=False,
                             widget=forms.EmailInput(attrs=
                                                     {'placeholder': 'joe@ejemplo.com',
                                                      'class': 'form-control'}))
    telefono = PhoneNumberField(required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Teléfono: +(999)999-9999',
               'class': 'form-control text_type_number',
               'id': 'txtPhone',
               }))
    servicios = forms.ModelMultipleChoiceField(queryset=Servicio.objects.all(),
                                               widget=forms.CheckboxSelectMultiple,
                                               required=True)

    class Meta:
        model = Cliente
        fields = ('__all__')
        widgets = {
            'comentariosCliente': Textarea(attrs={'placeholder': "Comentarios", 'cols': 48, 'rows': 5}),
            'fechaNacimiento': forms.DateInput(format=('%Y-%m-%d'),
                                               attrs={'class': 'form-control', 'placeholder': 'Fecha de nacimiento',
                                                      'type': 'date'}),

        }
