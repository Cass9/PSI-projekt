from rest_framework import serializers

from .models import Auto, Przeglad, Ubezpieczenie, Klient, Cennik, Wypozyczenia, Zwroty

class AutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auto
        fields = '__all__'

class PrzegladSerializer(serializers.ModelSerializer):
    class Meta:
        model = Przeglad
        fields = [
            'Data_poczatku_przegladu', 
            'Data_konca_przegladu', 
            'auto_id_auta'
        ]
        depth = 1

class UbezpieczenieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ubezpieczenie
        fields = [
            'auto_id_auta',
            'Data_konca_ubezpieczenia',
            'Data_poczatku_ubezpieczenia',
            'numer_ubezpieczenia',
            'Ubezpieczyciel',
            'cena_ubezpieczenia'
        ]
        depth = 1

class KlientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Klient
        fields = '__all__'

class CennikSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cennik
        fields = '__all__'

class WypozyczeniaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wypozyczenia
        fields = [
            'klient_id_klienta',
            'auto_id_auta',
            'data_wypozyczenia',
            'termin_zwrotu_zwrotu',
            'cennik_id_cennika'
        ]
        depth = 1

class ZwrotySerialiser(serializers.ModelSerializer):
    class Meta:
        model = Zwroty
        fields = [
            'wypozyczenia_id_wypozyczenia',
            'stan_licznika_po',
            'data_zwrotu'
        ]
        depth = 1


