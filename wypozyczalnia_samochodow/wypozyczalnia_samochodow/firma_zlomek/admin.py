from django.contrib import admin

# Register your models here.

from .models import Auto
from .models import Przeglad
from .models import Ubezpieczenie
from .models import Klient
from .models import Cennik
from .models import Wypozyczenia
from .models import Zwroty

admin.site.register(Auto)
admin.site.register(Przeglad)
admin.site.register(Ubezpieczenie)
admin.site.register(Klient)
admin.site.register(Cennik)
admin.site.register(Wypozyczenia)
admin.site.register(Zwroty)