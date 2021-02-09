from rest_framework import serializers

from .models import Auto, Przeglad, Ubezpieczenie, Klient, Cennik, Wypozyczenia, Zwroty 

from django.contrib.auth.models import User

class AutoSerializer(serializers.ModelSerializer):
    wlasciciel = serializers.ReadOnlyField(source='wlasciciel.username')
    class Meta:
        model = Auto
        fields = [    
            'Marka',
            'Model',
            'Rok_produkcji',
            'numer_rejestracyjny',
            'moc_silnika',
            'przebieg',
            'url',
            'wlasciciel'
        ]
      
        

class PrzegladSerializer(serializers.ModelSerializer):
    auto_id_auta = serializers.SlugRelatedField(queryset=Auto.objects.all(), slug_field='Model')
    
    class Meta:
        model = Przeglad
        fields = [
            'Data_poczatku_przegladu', 
            'Data_konca_przegladu', 
            'auto_id_auta',
            'url'
            
        ]
        

class UbezpieczenieSerializer(serializers.ModelSerializer):
    auto_id_auta = serializers.SlugRelatedField(queryset=Auto.objects.all(), slug_field='Model')
    class Meta:
        model = Ubezpieczenie
        fields = [
            'auto_id_auta',
            'Data_konca_ubezpieczenia',
            'Data_poczatku_ubezpieczenia',
            'numer_ubezpieczenia',
            'Ubezpieczyciel',
            'cena_ubezpieczenia',
            
        ]
        

class KlientSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Klient
        fields = [
            'Imie',
            'Nazwisko',
            'PESEL',
            'numer_dowodu_osobistego',
            'Miejscowosc',
            'Ulica',
            'Numer_domu',
            'Numer_mieszkania',
            'url'
            
        ]

class CennikSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cennik
        fields = [
            'Cena_za_dobe',
            'url'
        ]

class WypozyczeniaSerializer(serializers.ModelSerializer):
    klient_id_klienta = serializers.SlugRelatedField(queryset=Klient.objects.all(), slug_field='Imie')
    auto_id_auta = serializers.SlugRelatedField(queryset=Auto.objects.all(), slug_field='Model')
    cennik_id_cennika = serializers.SlugRelatedField(queryset=Cennik.objects.all(), slug_field='Cena_za_dobe')
    class Meta:
        model = Wypozyczenia
        fields = [
            'klient_id_klienta',
            'auto_id_auta',
            'data_wypozyczenia',
            'termin_zwrotu_zwrotu',
            'cennik_id_cennika',
            'url'
        ]
        
        #test23

class ZwrotySerialiser(serializers.ModelSerializer):
    wypozyczenia_id_wypozyczenia = serializers.SlugRelatedField(queryset=Wypozyczenia.objects.all(), slug_field='data_wypozyczenia')
    class Meta:
        model = Zwroty
        fields = [
            'wypozyczenia_id_wypozyczenia',
            'stan_licznika_po',
            'data_zwrotu',
            'url',
        ]
        
class UserAutoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Auto
        fields = ['url','Marka']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    auto = UserAutoSerializer(many=True, read_only = True)
    class Meta:
        model = User
        fields = ['url','username','auto']