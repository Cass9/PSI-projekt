from django.db import models

# Create your models here.

class Auto(models.Model):
    Marka= models.CharField(max_length=75, null=True)
    Model= models.CharField(max_length=75, null=True)
    Rok_produkcji= models.DateField(null=True)
    numer_rejestracyjny = models.CharField(max_length=75, null=False)
    moc_silnika = models.CharField(max_length=15, null=True)
    przebieg = models.FloatField(max_length=9, null=True)
    wlasciciel = models.ForeignKey('auth.User', related_name='auto', on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ('Marka',)

    def __str__(self):
        return self.Marka + ' ' + self.Model + ' ' + self.numer_rejestracyjny
    

class Przeglad(models.Model):
    Data_poczatku_przegladu = models.DateField()
    Data_konca_przegladu = models.DateField()
    auto_id_auta = models.ForeignKey(Auto, on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ('Data_konca_przegladu',)

    def __str__(self):
        return f"{self.auto_id_auta}, koniec ważności przeglądu dnia: {self.Data_konca_przegladu}"
    

class Ubezpieczenie(models.Model):
    auto_id_auta = models.ForeignKey(Auto, on_delete=models.SET_NULL, null=True)
    Data_konca_ubezpieczenia = models.DateField()
    Data_poczatku_ubezpieczenia = models.DateField()
    numer_ubezpieczenia = models.FloatField(max_length=20, null=False)
    Ubezpieczyciel = models.CharField(max_length=75, null=False)
    cena_ubezpieczenia = models.FloatField(max_length=5, null=False)

    class Meta:
        ordering = ('auto_id_auta',)

    def __str__(self):
        return f"{self.auto_id_auta}, koniec ważności ubezpieczenia dnia: {self.Data_konca_ubezpieczenia}"
    

class Klient(models.Model):
    Imie = models.CharField(max_length=75, null=False)
    Nazwisko = models.CharField(max_length=75, null=False)
    PESEL = models.FloatField(max_length=11, null=False)
    numer_dowodu_osobistego = models.FloatField(max_length=8, null=False)
    Miejscowosc = models.CharField(max_length=75, null=False)
    Ulica = models.CharField(max_length=75, null=True)
    Numer_domu = models.FloatField(max_length=3, null=True)
    Numer_mieszkania = models.FloatField(max_length=3, null=True)

    class Meta:
        ordering = ('Imie',)

    def __str__(self):
        return self.Imie + ' ' + self.Nazwisko
    

class Cennik(models.Model):
    Cena_za_dobe = models.FloatField(max_length=5, null=False)

    def __str__(self):
        return str(self.Cena_za_dobe)
    

class Wypozyczenia(models.Model):
    klient_id_klienta = models.ForeignKey(Klient, on_delete=models.SET_NULL, null=True)
    auto_id_auta = models.ForeignKey(Auto, on_delete=models.SET_NULL, null=True)
    data_wypozyczenia = models.DateField()
    termin_zwrotu_zwrotu = models.DateField()
    cennik_id_cennika = models.ForeignKey(Cennik, on_delete=models.SET_NULL, null=True) 

    class Meta:
        ordering = ('klient_id_klienta',)

    def __str__(self):
        return f"{self.klient_id_klienta}, wypożyczył samochod: {self.auto_id_auta}"
    

class Zwroty(models.Model):    
    wypozyczenia_id_wypozyczenia = models.ForeignKey(Wypozyczenia, on_delete=models.SET_NULL, null=True)
    stan_licznika_po = models.FloatField(max_length=3, null=False)
    data_zwrotu = models.DateField()

    class Meta:
        ordering = ('data_zwrotu',)

    def __str__(self):
        return str(self.wypozyczenia_id_wypozyczenia)
    