from django.contrib import admin

# Register your models here.

from .models import Auto, Przeglad, Ubezpieczenie, Klient, Cennik, Wypozyczenia, Zwroty

admin.site.register(Auto)
admin.site.register(Przeglad)
admin.site.register(Ubezpieczenie)
admin.site.register(Klient)
admin.site.register(Cennik)
admin.site.register(Wypozyczenia)
admin.site.register(Zwroty)