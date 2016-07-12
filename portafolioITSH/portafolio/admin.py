from django.contrib import admin
from django.forms import ModelForm, PasswordInput
from django import forms
from .models import Alumno
from .models import Usuario
from models import Asignatura


# Register your models here.
class UsuarioForm(ModelForm):
    class Meta:
		model = Usuario
		fields = ('nick', 'nombre','pass_field','tipo')
		widgets = {
            'pass_field': PasswordInput,
        }

class UsuarioAdmin(admin.ModelAdmin):
	list_display = ("nick","nombre","pass_field","tipo")
	search_fields = ('nombre',)
	list_filter = ('tipo',)
	form = UsuarioForm


class AsignaturaAdmin(admin.ModelAdmin):
	list_display = ("ngrupo","nick")
	raw_id_fields = ('nick',)

admin.site.register(Usuario,UsuarioAdmin)
admin.site.register(Asignatura,AsignaturaAdmin)
admin.site.register(Alumno)
