# Generated by Django 3.1.3 on 2020-12-06 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firma_zlomek', '0007_auto_20201207_0055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zwroty',
            name='stan_licznika_po',
            field=models.IntegerField(max_length=3),
        ),
    ]
