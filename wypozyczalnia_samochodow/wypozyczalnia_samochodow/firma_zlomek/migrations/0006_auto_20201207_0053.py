# Generated by Django 3.1.3 on 2020-12-06 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firma_zlomek', '0005_remove_auto_zdjecie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='klient',
            name='PESEL',
            field=models.BigIntegerField(max_length=11),
        ),
    ]