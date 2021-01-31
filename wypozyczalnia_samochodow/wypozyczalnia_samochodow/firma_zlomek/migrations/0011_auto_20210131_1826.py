# Generated by Django 3.1.3 on 2021-01-31 17:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('firma_zlomek', '0010_auto_20210127_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auto',
            name='Model',
            field=models.CharField(max_length=75, null=True),
        ),
        migrations.AlterField(
            model_name='auto',
            name='Rok_produkcji',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='auto',
            name='numer_rejestracyjny',
            field=models.CharField(max_length=75, null=True),
        ),
        migrations.AlterField(
            model_name='auto',
            name='przebieg',
            field=models.FloatField(max_length=9, null=True),
        ),
        migrations.AlterField(
            model_name='auto',
            name='wlasciciel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='auto', to=settings.AUTH_USER_MODEL),
        ),
    ]