from django.db import models

# Create your models here.
class Rol(models.Model):
    id_rol = models.AutoField(primary_key=True)
    nombre_rol = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_rol

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=100)
    contrasena = models.CharField(max_length=20)
    id_rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    nombre_usuario = models.CharField(max_length=100)
    apellido_usaurio = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.PositiveIntegerField()
    nit = models.CharField(max_length=100)

    def __str__(self):
        return "Nombre cliente: "+self.usuario +" Nit: "+self.nit

precio = 0
class Servicio(models.Model):
    id_servicio = models.AutoField(primary_key=True)
    nombre_servicio = models.CharField(max_length=100)
    precio_servicio = models.PositiveIntegerField()

    def __str__(self):
        precio = self.precio_servicio
        return "Tipo servicio: "+self.nombre_servicio

class Reservacion(models.Model):
    id_reservacion = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    fecha_hora_ingreso = models.DateTimeField()
    fecha_hora_salida = models.DateTimeField()
    total = models.PositiveIntegerField()

    def __str__(self):
        return "Reservacion usuario : "+ self.id_usuario.usuario +" Total: "+ str(self.total)
