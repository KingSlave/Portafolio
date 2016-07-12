# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models



class Alumno(models.Model):
    ncontrol = models.CharField(db_column='NCONTROL', primary_key=True, max_length=8)  # Field name made lowercase.
    apaterno = models.CharField(db_column='APATERNO', max_length=20)  # Field name made lowercase.
    amaterno = models.CharField(db_column='AMATERNO', max_length=20)  # Field name made lowercase.
    nombre = models.CharField(db_column='NOMBRE', max_length=30)  # Field name made lowercase.
    carrera = models.CharField(db_column='CARRERA', max_length=4)  # Field name made lowercase.
    pass_field = models.CharField(db_column='PASS', max_length=150, blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'alumno'


class Asignatura(models.Model):
    ngrupo = models.IntegerField(db_column='NGRUPO', primary_key=True)  # Field name made lowercase.
    nick = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='NICK', blank=True, null=True)  # Field name made lowercase.
    grupo = models.CharField(db_column='GRUPO', max_length=1, blank=True, null=True)  # Field name made lowercase.
    carrera = models.CharField(db_column='CARRERA', max_length=4, blank=True, null=True)  # Field name made lowercase.
    claveasignatura = models.CharField(db_column='CLAVEASIGNATURA', max_length=10, blank=True, null=True)  # Field name made lowercase.
    nombreasignatura = models.CharField(db_column='NOMBREASIGNATURA', max_length=60, blank=True, null=True)  # Field name made lowercase.
    semestre = models.IntegerField(db_column='SEMESTRE', blank=True, null=True)  # Field name made lowercase.
    unidades = models.IntegerField(db_column='UNIDADES', blank=True, null=True)  # Field name made lowercase.
    periodo = models.CharField(db_column='PERIODO', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'asignatura'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Evidencia(models.Model):
    ngrupo = models.ForeignKey(Asignatura, models.DO_NOTHING, db_column='NGRUPO')  # Field name made lowercase.
    nombre = models.CharField(db_column='NOMBRE', max_length=40)  # Field name made lowercase.
    nunidad = models.IntegerField(db_column='NUNIDAD')  # Field name made lowercase.
    valor = models.FloatField(db_column='VALOR', blank=True, null=True)  # Field name made lowercase.
    fechainicio = models.DateTimeField(db_column='FECHAINICIO', blank=True, null=True)  # Field name made lowercase.
    fechalimite = models.DateTimeField(db_column='FECHALIMITE', blank=True, null=True)  # Field name made lowercase.
    abierto = models.IntegerField(db_column='ABIERTO', blank=True, null=True)  # Field name made lowercase.
    linkrubrica = models.CharField(db_column='LINKRUBRICA', max_length=100, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='DESCRIPCION', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'evidencia'
        unique_together = (('ngrupo', 'nombre', 'nunidad'),)


class Lista(models.Model):
    folio = models.IntegerField(db_column='FOLIO', primary_key=True)  # Field name made lowercase.
    ncontrol = models.ForeignKey(Alumno, models.DO_NOTHING, db_column='NCONTROL', blank=True, null=True)  # Field name made lowercase.
    ngrupo = models.ForeignKey(Asignatura, models.DO_NOTHING, db_column='NGRUPO', blank=True, null=True)  # Field name made lowercase.
    complementacion = models.IntegerField(db_column='COMPLEMENTACION', blank=True, null=True)  # Field name made lowercase.
    promediofinal = models.FloatField(db_column='PROMEDIOFINAL', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lista'


class Portafolio(models.Model):
    ncontrol = models.ForeignKey(Alumno, models.DO_NOTHING, db_column='NCONTROL')  # Field name made lowercase.
    ngrupo = models.ForeignKey(Evidencia, models.DO_NOTHING, db_column='NGRUPO',related_name='portafolio_ngrupo')  # Field name made lowercase.
    nombre = models.ForeignKey(Evidencia, models.DO_NOTHING, db_column='NOMBRE',related_name='portafolio_nombre')  # Field name made lowercase.
    nunidad = models.ForeignKey(Evidencia, models.DO_NOTHING, db_column='NUNIDAD')  # Field name made lowercase.
    archivo = models.CharField(db_column='ARCHIVO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fechaentrega = models.DateTimeField(db_column='FECHAENTREGA', blank=True, null=True)  # Field name made lowercase.
    comentario = models.CharField(db_column='COMENTARIO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    calificacion = models.FloatField(db_column='CALIFICACION', blank=True, null=True)  # Field name made lowercase.
    observaciones = models.CharField(db_column='OBSERVACIONES', max_length=200, blank=True, null=True)  # Field name made lowercase.
    resultado = models.CharField(db_column='RESULTADO', max_length=40, blank=True, null=True)  # Field name made lowercase.
    fechareenvio = models.DateTimeField(db_column='FECHAREENVIO', blank=True, null=True)  # Field name made lowercase.
    numopor = models.IntegerField(db_column='NUMOPOR', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'portafolio'
        unique_together = (('ncontrol', 'ngrupo', 'nombre', 'nunidad'),)


class Usuario(models.Model):
    nick = models.CharField(db_column='NICK', primary_key=True, max_length=15,help_text = "Es usado para acceder al sistema")  # Field name made lowercase.
    nombre = models.CharField(db_column='NOMBRE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pass_field = models.CharField(db_column='PASS', max_length=150, blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    tipo = models.CharField(db_column='TIPO', max_length=50, blank=True, null=True,choices = (('docente','DOCENTE'),))  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usuario'
