from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Alumnos(models.Model):
    ncontrol = models.CharField(db_column='NCONTROL', primary_key=True, max_length=8)  # Field name made lowercase.
    apaterno = models.CharField(db_column='APATERNO', max_length=20)  # Field name made lowercase.
    amaterno = models.CharField(db_column='AMATERNO', max_length=20)  # Field name made lowercase.
    nombre = models.CharField(db_column='NOMBRE', max_length=30)  # Field name made lowercase.
    carrera = models.CharField(db_column='CARRERA', max_length=4)  # Field name made lowercase.
    pass_field = models.CharField(db_column='PASS', max_length=150, blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'alumnos'


class Asignaturas(models.Model):
    ngrupo = models.IntegerField(db_column='NGRUPO', primary_key=True)  # Field name made lowercase.
    nick = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='NICK', blank=True, null=True)  # Field name made lowercase.
    grupo = models.CharField(db_column='GRUPO', max_length=1, blank=True, null=True)  # Field name made lowercase.
    carrera = models.CharField(db_column='CARRERA', max_length=4, blank=True, null=True)  # Field name made lowercase.
    nombreasignatura = models.CharField(db_column='NOMBREASIGNATURA', max_length=60, blank=True, null=True)  # Field name made lowercase.
    semestre = models.IntegerField(db_column='SEMESTRE', blank=True, null=True)  # Field name made lowercase.
    unidades = models.IntegerField(db_column='UNIDADES', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'asignaturas'


class Evidencias(models.Model):
    nevidencia = models.IntegerField(db_column='NEVIDENCIA', primary_key=True)  # Field name made lowercase.
    ngrupo = models.ForeignKey(Asignaturas, models.DO_NOTHING, db_column='NGRUPO', blank=True, null=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='NOMBRE', max_length=40, blank=True, null=True)  # Field name made lowercase.
    valor = models.FloatField(db_column='VALOR', blank=True, null=True)  # Field name made lowercase.
    nunidad = models.IntegerField(db_column='NUNIDAD', blank=True, null=True)  # Field name made lowercase.
    fechainicio = models.DateTimeField(db_column='FECHAINICIO', blank=True, null=True)  # Field name made lowercase.
    fechalimite = models.DateTimeField(db_column='FECHALIMITE', blank=True, null=True)  # Field name made lowercase.
    abierto = models.IntegerField(db_column='ABIERTO', blank=True, null=True)  # Field name made lowercase.
    linkrubrica = models.CharField(db_column='LINKRUBRICA', max_length=100, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='DESCRIPCION', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'evidencias'


class Listas(models.Model):
    folio = models.IntegerField(db_column='FOLIO', primary_key=True)  # Field name made lowercase.
    ncontrol = models.ForeignKey(Alumnos, models.DO_NOTHING, db_column='NCONTROL', blank=True, null=True)  # Field name made lowercase.
    ngrupo = models.ForeignKey(Asignaturas, models.DO_NOTHING, db_column='NGRUPO', blank=True, null=True)  # Field name made lowercase.
    complementacion = models.IntegerField(db_column='COMPLEMENTACION', blank=True, null=True)  # Field name made lowercase.
    promediofinal = models.FloatField(db_column='PROMEDIOFINAL', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'listas'


class Portafolios(models.Model):
    ncontrol = models.ForeignKey(Alumnos, models.DO_NOTHING, db_column='NCONTROL')  # Field name made lowercase.
    nevidencia = models.ForeignKey(Evidencias, models.DO_NOTHING, db_column='NEVIDENCIA')  # Field name made lowercase.
    archivo = models.CharField(db_column='ARCHIVO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fechaentrega = models.DateTimeField(db_column='FECHAENTREGA', blank=True, null=True)  # Field name made lowercase.
    comentario = models.CharField(db_column='COMENTARIO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    calificacion = models.FloatField(db_column='CALIFICACION', blank=True, null=True)  # Field name made lowercase.
    observaciones = models.CharField(db_column='OBSERVACIONES', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'portafolios'
        unique_together = (('ncontrol', 'nevidencia'),)


class Usuarios(models.Model):
    nick = models.CharField(db_column='NICK', primary_key=True, max_length=15)  # Field name made lowercase.
    nombre = models.CharField(db_column='NOMBRE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pass_field = models.CharField(db_column='PASS', max_length=150, blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    tipo = models.CharField(db_column='TIPO', max_length=50, blank=True, null=True,choices=[('profesor','Docente'), ('admin', 'Administrador')])  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usuarios'
