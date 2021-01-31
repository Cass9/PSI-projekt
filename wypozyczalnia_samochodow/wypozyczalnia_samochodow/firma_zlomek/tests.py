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
        assert Auto.objects.get().name == nowa_marka   

class 