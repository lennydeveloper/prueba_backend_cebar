from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Departamento(models.Model):
    nombre = models.CharField('Nombre', db_column='nombre', max_length=50, editable=True, blank=False, null=False)

    class Meta:
       db_table = "departamento"
       verbose_name = "departamento"
       verbose_name_plural = "departamentos"
       ordering = ['id']
    
    def __str__(self):
       return f'id: {self.id}, nombre: {self.nombre}'

class Municipio(models.Model):
    nombre = models.CharField('Nombre', db_column='nombre', max_length=50, editable=True, blank=False, null=False)
    id_fk_departamento = models.ForeignKey(Departamento, db_column='id_fk_departamento', on_delete=models.DO_NOTHING, null=False, blank=False)

    class Meta:
       db_table = "municipio"
       verbose_name = "municipio"
       verbose_name_plural = "municipios"
       ordering = ['id']
    
    def __str__(self):
       return f'id: {self.id}, nombre: {self.nombre}'

class User(AbstractUser):
    roles = (
        (1, 'ADMIN'),
        (2, 'LIDER')
    )

    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    rol = models.PositiveSmallIntegerField(choices=roles, blank=False, null=False, default=2)
    username = None,
    user_picture = models.BinaryField(null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Comuna(models.Model):
    nombre = models.CharField('Nombre', db_column='nombre', max_length=50, editable=True, blank=False, null=False)
    id_fk_municipio = models.ForeignKey(Municipio, db_column='id_fk_municipio', on_delete=models.DO_NOTHING, null=False, blank=False)

    class Meta:
       db_table = "comuna"
       verbose_name = "comuna"
       verbose_name_plural = "comunas"
       ordering = ['id']
    
    def __str__(self):
       return f'id: {self.id}, nombre: {self.nombre}'

class Barrio(models.Model):
    nombre = models.CharField('Nombre', db_column='nombre', max_length=50, editable=True, blank=False, null=False)
    id_fk_comuna = models.ForeignKey(Comuna, db_column='id_fk_comuna', on_delete=models.DO_NOTHING, null=False, blank=False)

    class Meta:
       db_table = "barrio"
       verbose_name = "barrio"
       verbose_name_plural = "barrios"
       ordering = ['id']
    
    def __str__(self):
       return self.nombre

class PuestoVotacion(models.Model):
    nombre = models.CharField('Nombre', db_column='nombre', max_length=50, editable=True, blank=False, null=False)
    direccion = models.CharField('Direccion', db_column='direccion', max_length=100, editable=True, blank=False, null=False)
    id_fk_municipio = models.ForeignKey(Municipio, db_column='id_fk_municipio', on_delete=models.DO_NOTHING, null=False, blank=False)
    id_fk_usuario = models.ForeignKey(User, db_column='id_fk_usuario', on_delete=models.DO_NOTHING, null=False, blank=False)

    class Meta:
       db_table = "puesto_votacion"
       verbose_name = "puesto votación"
       verbose_name_plural = "puestos de votación"
       ordering = ['id']
    
    def __str__(self):
       return self.nombre

class Votante(models.Model):
    nombre = models.CharField('Nombre', db_column='nombre', max_length=50, editable=True, blank=False, null=False)
    apellido = models.CharField('Apellido', db_column='apellido', max_length=50, editable=True, blank=False, null=False)
    direccion = models.CharField('Dirección', db_column='direccion', max_length=100, editable=True, blank=False, null=False)
    telefono = models.CharField('Teléfono', db_column='telefono', max_length=10, editable=True, blank=False, null=False)
    cedula = models.CharField('Cédula', db_column='cedula', max_length=10, editable=True, blank=False, null=False)
    id_fk_usuario = models.ForeignKey(User, db_column='id_fk_usuario', on_delete=models.DO_NOTHING, null=False, blank=False)
    id_fk_barrio = models.ForeignKey(Barrio, db_column='id_fk_barrio', on_delete=models.DO_NOTHING, null=False, blank=False)
    id_fk_puesto_votacion = models.ForeignKey(PuestoVotacion, db_column='id_fk_puesto_votacion', on_delete=models.DO_NOTHING, null=False, blank=False)
    mesa = models.IntegerField('Mesa', db_column='mesa', editable=True, null=True, blank=True)

    class Meta:
       db_table = "votante"
       verbose_name = "votante"
       verbose_name_plural = "votantes"
       ordering = ['id']

    def __str__(self):
        return f'id: {self.id}, nombre: {self.nombre} {self.apellido}'

class Traza(models.Model):
   id_fk_usuario = models.ForeignKey(User, db_column='id_fk_usuario', on_delete=models.DO_NOTHING, null=False, blank=False)
   id_fk_votante = models.ForeignKey(Votante, db_column='id_fk_votante', on_delete=models.DO_NOTHING, null=False, blank=False)
   fecha_registro = models.DateTimeField(auto_now_add=True)
   descripcion = models.CharField(db_column='descripcion', max_length=200, null=True, blank=True)

   class Meta:
      db_table = "traza"
      verbose_name = "traza"
      verbose_name_plural = "trazas"
      ordering = ['id']

   def __str__(self):
      return f'id: {self.id}, fecha_registro: {self.fecha_registro}'