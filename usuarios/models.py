

from django.db import models

class Usuarios(models.Model):
    # Supongo que "rut" es el número de identificación único, por lo que se establece como clave primaria.
    rut = models.CharField(primary_key=True, max_length=20)
    nombre = models.CharField(max_length=20)
    apellidop = models.CharField(max_length=20)
    apellidom = models.CharField(max_length=20)
    direccion = models.CharField(max_length=20)
    comuna = models.CharField(max_length=20)
    ciudad = models.CharField(max_length=20)
    telefono = models.IntegerField()  # Campo de número entero para el teléfono
    correo = models.EmailField()  # Campo de correo electrónico
    # Para el campo "tipoEmpleado" como ComboBox, puedes usar un campo de elección.
    # Define las opciones para el ComboBox.
    TIPO_EMPLEADO_CHOICES = (
        ('Admin', 'Admin'),
        ('Empleado', 'Empleado'),

    )
    tipoEmpleado = models.CharField(max_length=20, choices=TIPO_EMPLEADO_CHOICES)

    def __str__(self):
        return self.nombre  # Puedes personalizar esto para mostrar información relevante en la representación de objetos.

