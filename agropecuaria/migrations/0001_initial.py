# Generated by Django 3.1.1 on 2020-09-27 04:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id_rol', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_rol', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id_servicio', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_servicio', models.CharField(max_length=100)),
                ('precio_servicio', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('usuario', models.CharField(max_length=100)),
                ('contrasena', models.CharField(max_length=20)),
                ('nombre_usuario', models.CharField(max_length=100)),
                ('apellido_usaurio', models.CharField(max_length=100)),
                ('correo', models.EmailField(max_length=254)),
                ('telefono', models.PositiveIntegerField()),
                ('nit', models.CharField(max_length=100)),
                ('id_rol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agropecuaria.rol')),
            ],
        ),
        migrations.CreateModel(
            name='Reservacion',
            fields=[
                ('id_reservacion', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_hora_ingreso', models.DateTimeField()),
                ('fecha_hora_salida', models.DateTimeField()),
                ('total', models.PositiveIntegerField()),
                ('id_servicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agropecuaria.servicio')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agropecuaria.usuario')),
            ],
        ),
    ]
