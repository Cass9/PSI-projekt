# Generated by Django 3.1.3 on 2020-12-07 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firma_zlomek', '0008_auto_20201207_0057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auto',
            name='przebieg',
            field=models.FloatField(max_length=9),
        ),
        migrations.AlterField(
            model_name='klient',
            name='Numer_domu',
            field=models.FloatField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='klient',
            name='Numer_mieszkania',
            field=models.FloatField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='klient',
            name='PESEL',
            field=models.FloatField(max_length=11),
        ),
        migrations.AlterField(
            model_name='klient',
            name='numer_dowodu_osobistego',
            field=models.FloatField(max_length=8),
        ),
        migrations.AlterField(
            model_name='ubezpieczenie',
            name='numer_ubezpieczenia',
            field=models.FloatField(max_length=20),
        ),
        migrations.AlterField(
            model_name='zwroty',
            name='stan_licznika_po',
            field=models.FloatField(max_length=3),
        ),
    ]
