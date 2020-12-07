from rest_framework import serializers

from .models import Auto, Przeglad, Ubezpieczenie, Klient, Cennik, Wypozyczenia, Zwroty

class AutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auto
        fields = '__all__'

class PrzegladSerializer(serializers.ModelSerializer):
    class Meta:
        model = Przeglad
        fields = '__all__'

class UbezpieczenieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ubezpieczenie
        fields = '__all__'

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
        fields = '__all__'

class ZwrotySerialiser(serializers.ModelSerializer):
    class Meta:
        model = Zwroty
        fields = '__all__'


