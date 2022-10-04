from django.contrib import admin
from django import forms
from .models import Votante
import re

# Register your models here.
class VotantesAdminForm(forms.ModelForm):
    def clean_cedula(self):
        """
        Validar que la cédula no se encuentre registrada en el sistema
        """
        count_votantes = Votante.objects.filter(cedula=self.cleaned_data['cedula']).count()
        if count_votantes > 0:
            raise forms.ValidationError(f"El documento {self.cleaned_data['cedula']} ya se encuentra registrado")

        pattern = r"^[0-9]*$"
        cedula = self.cleaned_data['cedula']
        if re.match(pattern, cedula):
            if len(cedula) >= 8 and len(cedula) <= 10:
                return self.cleaned_data['cedula']
            else:
                raise forms.ValidationError(f'El número de documento no cumple con el formato de DNI')

class VotantesAdmin(admin.ModelAdmin):
    form = VotantesAdminForm
    list_filter = ('cedula', 'id_fk_puesto_votacion', 'mesa')
    list_display = ('nombre', 'apellido', 'direccion', 'telefono', 'cedula', 'id_fk_usuario', 'id_fk_barrio', 'id_fk_puesto_votacion', 'mesa')
    search_fields = ('cedula', 'id_fk_puesto_votacion', 'mesa')

admin.site.register(Votante, VotantesAdmin)