# Generated by Django 3.1.3 on 2020-12-06 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firma_zlomek', '0006_auto_20201207_0053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auto',
            name='przebieg',
            field=models.BigIntegerField(max_length=9),
        ),
        migrations.AlterField(
            model_name='ubezpieczenie',
            name='numer_ubezpieczenia',
            field=models.BigIntegerField(max_length=20),
        ),
        migrations.AlterField(
            model_name='zwroty',
            name='stan_licznika_po',
            field=models.BigIntegerField(max_length=3),
        ),
    ]
