# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Alumno(models.Model):
    codigoalumno = models.IntegerField(db_column='codigoAlumno', primary_key=True)  # Field name made lowercase.
    dnialumno = models.IntegerField(db_column='dniAlumno', unique=True)  # Field name made lowercase.
    nombresalumno = models.CharField(db_column='nombresAlumno', max_length=45)  # Field name made lowercase.
    apellidosalumno = models.CharField(db_column='apellidosAlumno', max_length=45)  # Field name made lowercase.
    facultad = models.CharField(max_length=45)
    escuela = models.CharField(max_length=45)
    sexo = models.CharField(max_length=45, blank=True, null=True)
    telefono = models.CharField(max_length=45, blank=True, null=True)
    direccion = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Alumno'
