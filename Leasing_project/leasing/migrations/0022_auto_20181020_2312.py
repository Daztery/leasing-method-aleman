# Generated by Django 2.1.1 on 2018-10-21 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leasing', '0021_auto_20181020_2134'),
    ]

    operations = [
        migrations.AddField(
            model_name='prestamo',
            name='tasa_descuento_Ks',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='prestamo',
            name='tasa_descuento_WACC',
            field=models.FloatField(null=True),
        ),
    ]
