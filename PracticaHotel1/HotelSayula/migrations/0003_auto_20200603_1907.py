# Generated by Django 2.2.6 on 2020-06-04 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HotelSayula', '0002_auto_20200416_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habitacione',
            name='Numero_Habitaciones',
            field=models.IntegerField(db_column='Numero_Habitaciones', primary_key=True, serialize=False),
        ),
    ]