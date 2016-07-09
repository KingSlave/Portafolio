from django.contrib import admin
from .models import Alumnos
from .models import Usuarios
from models import Asignaturas

# Register your models here.
class UsuariosAdmin(admin.ModelAdmin):
	list_display = ("nick","nombre","pass_field","tipo")
	search_fields = ('nombre',)
	list_filter = ('tipo',)
		

class AsignaturasAdmin(admin.ModelAdmin):
	list_display = ("ngrupo","nick")
	raw_id_fields = ('nick',)
		
admin.site.register(Usuarios,UsuariosAdmin)
admin.site.register(Asignaturas,AsignaturasAdmin)
admin.site.register(Alumnos)