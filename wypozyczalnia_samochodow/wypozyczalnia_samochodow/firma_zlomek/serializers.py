from rest_framework import serializers

from .models import Auto, Przeglad, Ubezpieczenie, Klient, Cennik, Wypozyczenia, Zwroty

class AutoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    Marka = serializers.CharField(required=True, max_lenght=75)
    Model = serializers.CharField(required=True, max_lenght=75)
    Rok_produkcji = serializers.DateField(required=True)
    numer_rejestracyjny = serializers.CharField(required=True, max_lenght=75)
    moc_silnika = serializers.CharField(required=False, max_lenght=15)
    przebieg = serializers.IntegerField(required=True, max_lenght=9)

    def create(self, validated_data): 
        return Auto.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.Marka = validated_data.get('Marka', instance.Marka)
        instance.Model = validated_data.get('Model', instance.Model)
        instance.Rok_produkcji = validated_data.get('Rok_produkcji', instance.Rok_produkcji)
        instance.numer_rejestracyjny = validated_data.get('numer_rejestracyjny', instance.numer_rejestracyjny)
        instance.moc_silnika = validated_data.get('moc_silnika', instance.moc_silnika)
        instance.przebieg = validated_data.get('przebieg', instance.przebieg)
        instance.save()

        return instance


