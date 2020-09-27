from django.contrib import admin
from .models import Reservacion, Servicio, Rol, Usuario

# Register your models here.
admin.site.register(Reservacion)
admin.site.register(Servicio)
admin.site.register(Rol)
admin.site.register(Usuario)
