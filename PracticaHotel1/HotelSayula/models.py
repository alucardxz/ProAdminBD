from django.db import models
# Create your models here.
class Cliente(models.Model):
    Id_Cliente = models.IntegerField(db_column='Id_Cliente', primary_key=True)  # Field name made lowercase.
    NombreC = models.CharField(db_column='NombC', max_length=30, blank=True, null=True)  # Field name made lowercase.
    AP_C = models.CharField(db_column='AP_C', max_length=30, blank=True, null=True)  # Field name made lowercase.
    AM_M = models.CharField(db_column='AM_M', max_length=30, blank=True, null=True)  # Field name made lowercase.
    TCel_C = models.IntegerField(db_column='TCel_C',blank=True, null=True)  # Field name made lowercase.
    TCasa_C = models.IntegerField(db_column='TCasa_C', blank=True, null=True)  # Field name made lowercase.
    Cantidad_Personas = models.IntegerField(db_column='Cantidad de personas', blank=True, null=True)  # Field name made lowercase.
    Ciudad=models.CharField(db_column='Ciudad', max_length=15, blank=True, null=True)
    Estado=models.CharField(db_column='Estado', max_length=15, blank=True, null=True)
    Pais=models.CharField(db_column='Pais', max_length=15, blank=True, null=True)
    Numero_Habitaciones=models.IntegerField(db_column='Numero_Habitaciones', blank=True, null=True)  
    class meta:
        managed = False
        db_table = 'clientes'

class Ciudade(models.Model):
    Id_Ciudad = models.IntegerField(db_column='Id_Ciudad', primary_key=True)  # Field name made lowercase.
    Nombre_C = models.CharField(db_column='Nomb_C', max_length=15, blank=True, null=True)  # Field name made lowercase.
    class meta:
        managed = False
        db_table = 'ciudad'
class Estado(models.Model):
    Id_Estado= models.IntegerField(db_column='Id_Ciudad', primary_key=True)  # Field name made lowercase.
    Nombre_E = models.CharField(db_column='Nomb_E', max_length=15, blank=True, null=True)  # Field name made lowercase.
    class meta:
        managed = False
        db_table = 'estado'
class Pai(models.Model):
    Id_Pais = models.IntegerField(db_column='Id_Ciudad', primary_key=True)  # Field name made lowercase.
    Nombre_P = models.CharField(db_column='Nomb_C', max_length=15, blank=True, null=True)  # Field name made lowercase.
    class meta:
        managed = False
        db_table = 'pais'
class Habitacione(models.Model):
    Numero_Habitaciones = models.IntegerField(db_column='Numero_Habitaciones', primary_key=True)  # Field name made lowercase.
    Precio= models.FloatField(db_column='NombC',blank=True, null=True)  # Field name made lowercase.
    Disponibilidad = models.BooleanField(db_column='AP_C',  blank=True, null=True)  # Field name made lowercase.
    Tipo = models.CharField(db_column='AM_M', max_length=30, blank=True, null=True)  # Field name made lowercase.
    Descripcion = models.CharField(db_column='Sexo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    class meta:
        managed = False
        db_table = 'habitaciones'
class Reservacione(models.Model):
    Id_Reservacion = models.IntegerField(db_column='Id_Reservacion', primary_key=True)  # Field name made lowercase.
    Fecha_Reservacion= models.DateField(db_column='Fecha_Reservacion',  blank=True, null=True)  # Field name made lowercase.
    Fecha_Entrada = models.DateField(db_column='Fecha_Entrada', blank=True, null=True)  # Field name made lowercase.
    Fecha_Salida = models.DateField(db_column='Fecha_Salida',blank=True, null=True)  # Field name made lowercase.
    Total = models.FloatField(db_column='Total',  blank=True, null=True)
    Subtotal=models.FloatField(db_column='Subtotal', blank=True, null=True)
    class meta:
        managed = False
        db_table = 'reservaciones'
class Recepcionista(models.Model):
    Id_Empleado = models.IntegerField(db_column='Id_Empleado', primary_key=True)  # Field name made lowercase.
    Nombre_R = models.CharField(db_column='Nombre_R', max_length=30, blank=True, null=True)  # Field name made lowercase.
    AP_R = models.CharField(db_column='AP_C', max_length=30, blank=True, null=True)  # Field name made lowercase.
    AM_R = models.CharField(db_column='AM_M', max_length=30, blank=True, null=True)  # Field name made lowercase.
    Turno = models.CharField(db_column='Sexo', max_length=30, blank=True, null=True)  # Field name made lowercase.
    class meta:
        managed = False
        db_table = 'recepcionistas'