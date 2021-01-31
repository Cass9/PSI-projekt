from django.test import TestCase
from . import views
from .models import Auto
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
# Create your tests here.


class AutoTests(APITestCase):
    def post_Auto(self, numer_rejestracyjny):
        url = reverse(views.AutoList.name)
        data = {'numer_rejestracyjny':numer_rejestracyjny}
        response = self.client.post(url, data,format='json')
        return response

    def test_post_and_get_auto(self):
        nowa_marka = 'Bugatti'
        response = self.post_Auto(nowa_marka)
        assert response.status_code == status.HTTP_201_CREATED
        assert Auto.objects.count() == 1
        assert Auto.objects.get().nowa_marka == nowa_marka   

class KlienTest(APITestCase):
    def post_Klient(self, Imie, Nazwisko, PESEL, numer_dowodu_osobistego, Miejscowosc):
        url = reverse(views.KlientList.name)
        data = {'imie':Imie, 'nazwisko':Nazwisko, 'PESEL':PESEL, 'numer_dowodu_osobistego':numer_dowodu_osobistego, 'miejscowosc':Miejscowosc}
        response = self.client.post(url, data, format='json')
        return response

    def test_post_and_get_klient(self):
        nowe_imie='Kamil'
        nowe_nazwisko='Wytry'
        nowy_PESEL='98080804182'
        nowy_numer_dowodu_osobistego='CDF2019232'
        nowa_miejscowosc='Bielawa'
        response = self.post_Klient(nowe_imie, nowe_nazwisko, nowy_PESEL, nowy_numer_dowodu_osobistego, nowa_miejscowosc)
        assert response.status_code == status.HTTP_201_CREATED
        assert Klient.objects.count() == 2
        assert Klient.objects.get().imie == nowe_imie
        assert Klient.objects.get().nazwisko == nowe_nazwisko
        assert Klient.objects.get().PESEL == nowy_PESEL
        assert Klient.objects.get().numer_dowodu_osobistego == nowy_numer_dowodu_osobistego
        assert Klient.objects.get().nowa_miejscowosc == nowa_miejscowosc  