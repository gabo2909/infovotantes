from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Departamento(models.Model):
    nombre = models.CharField('Nombre', db_column='nombre', max_length=50, editable=True, blank=False, null=False)

    class Meta:
       db_table = "departamento"
       verbose_name = "Departamento"
       verbose_name_plural = "Departamentos"
       ordering = ['id']
    
    def __str__(self):
       return f'id: {self.id}, nombre: {self.nombre}'

class Municipio(models.Model):
    nombre = models.CharField('Nombre', db_column='nombre', max_length=50, editable=True, blank=False, null=False)
    id_fk_departamento = models.ForeignKey(Departamento, db_column='id_fk_departamento', on_delete=models.PROTECT, null=False, blank=False)

    class Meta:
       db_table = "municipio"
       verbose_name = "Municipio"
       verbose_name_plural = "Municipios"
       ordering = ['id']
    
    def __str__(self):
       return f'id: {self.id}, nombre: {self.nombre}'

class User(AbstractUser):
    ROL_CHOICES = (
        (1, 'ADMIN'),
        (2, 'LIDER')
    )

    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    rol = models.PositiveSmallIntegerField(choices=ROL_CHOICES, blank=False, null=False, default=2)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Comuna(models.Model):
    nombre = models.CharField('Nombre', db_column='nombre', max_length=50, editable=True, blank=False, null=False)
    id_fk_municipio = models.ForeignKey(Municipio, db_column='id_fk_municipio', on_delete=models.PROTECT, null=False, blank=False)

    class Meta:
       db_table = "comuna"
       verbose_name = "Comuna"
       verbose_name_plural = "Comunas"
       ordering = ['id']
    
    def __str__(self):
       return f'id: {self.id}, nombre: {self.nombre}'

class Barrio(models.Model):
    nombre = models.CharField('Nombre', db_column='nombre', max_length=50, editable=True, blank=False, null=False)
    id_fk_comuna = models.ForeignKey(Comuna, db_column='id_fk_comuna', on_delete=models.PROTECT, null=False, blank=False)

    class Meta:
       db_table = "barrio"
       verbose_name = "Barrio"
       verbose_name_plural = "Barrios"
       ordering = ['id']
    
    def __str__(self):
       return f'id: {self.id}, nombre: {self.nombre}'

class PuestoVotacion(models.Model):
    nombre = models.CharField('Nombre', db_column='nombre', max_length=50, editable=True, blank=False, null=False)
    direccion = models.CharField('Direccion', db_column='direccion', max_length=100, editable=True, blank=False, null=False)
    id_fk_municipio = models.ForeignKey(Municipio, db_column='id_fk_municipio', on_delete=models.PROTECT, null=False, blank=False)
    id_fk_usuario = models.ForeignKey(User, db_column='id_fk_usuario', on_delete=models.PROTECT, null=False, blank=False)

    class Meta:
       db_table = "puesto_votacion"
       verbose_name = "Puesto votación"
       verbose_name_plural = "Puestos de votación"
       ordering = ['id']
    
    def __str__(self):
       return f'id: {self.id}, nombre: {self.nombre}, dirección: {self.direccion}'

class Votante(models.Model):
    nombre = models.CharField('Nombre', db_column='nombre', max_length=50, editable=True, blank=False, null=False)
    apellido = models.CharField('Apellido', db_column='apellido', max_length=50, editable=True, blank=False, null=False)
    direccion = models.CharField('Dirección', db_column='direccion', max_length=100, editable=True, blank=False, null=False)
    telefono = models.CharField('Teléfono', db_column='telefono', max_length=10, editable=True, blank=False, null=False)
    cedula = models.CharField('Cédula', db_column='cedula', max_length=10, editable=True, blank=False, null=False)
    id_fk_usuario = models.ForeignKey(User, db_column='id_fk_usuario', on_delete=models.PROTECT, null=False, blank=False)
    id_fk_barrio = models.ForeignKey(Barrio, db_column='id_fk_barrio', on_delete=models.PROTECT, null=False, blank=False)
    id_fk_puesto_votacion = models.ForeignKey(PuestoVotacion, db_column='id_fk_puesto_votacion', on_delete=models.PROTECT, null=False, blank=False)
    mesa = models.IntegerField('Mesa', db_column='mesa', editable=True, null=True, blank=True)

    class Meta:
       db_table = "votante"
       verbose_name = "Votante"
       verbose_name_plural = "Votantes"
       ordering = ['id']

    def __str__(self):
        return f'id: {self.id}, nombre: {self.nombre} {self.apellido}'

class Traza(models.Model):
   id_fk_usuario = models.ForeignKey(User, db_column='id_fk_usuario', on_delete=models.DO_NOTHING, null=False, blank=False)
   id_fk_votante = models.ForeignKey(Votante, db_column='id_fk_votante', on_delete=models.DO_NOTHING, null=False, blank=False)
   fecha_registro = models.DateTimeField(auto_now_add=True)

   class Meta:
      db_table = "traza"
      verbose_name = "traza"
      verbose_name_plural = "trazas"
      ordering = ['id']

   def __str__(self):
      return f'id: {self.id}, fecha_registro: {self.fecha_registro}'