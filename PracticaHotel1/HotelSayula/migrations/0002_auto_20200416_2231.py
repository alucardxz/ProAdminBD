# Generated by Django 2.2.6 on 2020-04-17 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HotelSayula', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('Id_Cliente', models.IntegerField(db_column='Id_Cliente', primary_key=True, serialize=False)),
                ('NombreC', models.CharField(blank=True, db_column='NombC', max_length=30, null=True)),
                ('AP_C', models.CharField(blank=True, db_column='AP_C', max_length=30, null=True)),
                ('AM_M', models.CharField(blank=True, db_column='AM_M', max_length=30, null=True)),
                ('TCel_C', models.IntegerField(blank=True, db_column='TCel_C', null=True)),
                ('TCasa_C', models.IntegerField(blank=True, db_column='TCasa_C', null=True)),
                ('Cantidad_Personas', models.IntegerField(blank=True, db_column='Cantidad de personas', null=True)),
                ('Ciudad', models.CharField(blank=True, db_column='Ciudad', max_length=15, null=True)),
                ('Estado', models.CharField(blank=True, db_column='Estado', max_length=15, null=True)),
                ('Pais', models.CharField(blank=True, db_column='Pais', max_length=15, null=True)),
                ('Numero_Habitaciones', models.IntegerField(blank=True, db_column='Numero_Habitaciones', null=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='Ciudad',
            new_name='Ciudade',
        ),
        migrations.RenameModel(
            old_name='Habitaciones',
            new_name='Habitacione',
        ),
        migrations.RenameModel(
            old_name='Pais',
            new_name='Pai',
        ),
        migrations.RenameModel(
            old_name='Recepcionistas',
            new_name='Recepcionista',
        ),
        migrations.RenameModel(
            old_name='Reservaciones',
            new_name='Reservacione',
        ),
        migrations.DeleteModel(
            name='Clientes',
        ),
        migrations.RemoveField(
            model_name='estado',
            name='Nombre_C',
        ),
        migrations.AddField(
            model_name='estado',
            name='Nombre_E',
            field=models.CharField(blank=True, db_column='Nomb_E', max_length=15, null=True),
        ),
    ]
