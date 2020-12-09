from django.shortcuts import render
from django.http import HttpResponse
from .serializers import AutoSerializer
from .serializers import KlientSerializer
from .serializers import PrzegladSerializer
from .serializers import UbezpieczenieSerializer
from .serializers import CennikSerializer
from .serializers import WypozyczeniaSerializer
from .serializers import ZwrotySerialiser
from rest_framework import generics
from rest_framework.reverse import reverse
from .models import Auto
from .models import Klient
from .models import Przeglad
from .models import Ubezpieczenie
from .models import Cennik
from .models import Wypozyczenia
from .models import Zwroty
from rest_framework.response import Response


# Create your views here.

def index(request):
    return HttpResponse("Wypożyczalnia samochodów")


class AutoList(generics.ListCreateAPIView):
    queryset = Auto.objects.all()
    serializer_class = AutoSerializer
    name = 'auto-list'

class AutoDetail(generics.RetrieveDestroyAPIView):
    queryset = Auto.objects.all()
    serializer_class = AutoSerializer
    name = 'auto-detail'

class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({'api-root': reverse(AutoList.name, request=request),
                         'klient': reverse(KlientList.name, request=request),
                         'przeglad': reverse(PrzegladList.name, request=request),
                         'ubezpieczenie':reverse(UbezpieczenieList.name, request=request),
                         'cennik': reverse(CennikList.name, request=request),
                         'wypozyczenia': reverse(WypozyczeniaList.name, request=request),
                         'zwroty':reverse(ZwrotyList.name, request=request)
                         })
       


class KlientList(generics.ListCreateAPIView):
    queryset = Klient.objects.all()
    serializer_class = KlientSerializer
    name = 'klient-list'

class KlientDetail(generics.RetrieveDestroyAPIView):
    queryset = Klient.objects.all()
    serializer_class = KlientSerializer
    name = 'klient-detail'


class PrzegladList(generics.ListCreateAPIView):
    queryset = Przeglad.objects.all()
    serializer_class = PrzegladSerializer
    name = 'przeglad-list'

class PrzegladDetail(generics.RetrieveDestroyAPIView):
    queryset = Przeglad.objects.all()
    serializer_class = PrzegladSerializer
    name = 'przeglad-detail'



class UbezpieczenieList(generics.ListCreateAPIView):
    queryset = Ubezpieczenie.objects.all()
    serializer_class = UbezpieczenieSerializer
    name = 'ubezpieczenie-list'

class UbezpieczenieDetail(generics.RetrieveDestroyAPIView):
    queryset = Ubezpieczenie.objects.all()
    serializer_class = UbezpieczenieSerializer
    name = 'ubezpieczenie-detail'

    
class CennikList(generics.ListCreateAPIView):
    queryset = Cennik.objects.all()
    serializer_class = CennikSerializer
    name = 'cennik-list'

class CennikDetail(generics.RetrieveDestroyAPIView):
    queryset = Cennik.objects.all()
    serializer_class = CennikSerializer
    name = 'cennik-detail'

class WypozyczeniaList(generics.ListCreateAPIView):
    queryset = Wypozyczenia.objects.all()
    serializer_class = WypozyczeniaSerializer
    name = 'wypozyczenia-list'

class WypozyczeniaDetail(generics.RetrieveDestroyAPIView):
    queryset = Wypozyczenia.objects.all()
    serializer_class = WypozyczeniaSerializer
    name = 'wypozyczenia-detail'

class ZwrotyList(generics.ListCreateAPIView):
    queryset = Zwroty.objects.all()
    serializer_class = ZwrotySerialiser
    name = 'zwroty-list'

class ZwrotyDetail(generics.RetrieveDestroyAPIView):
    queryset = Zwroty.objects.all()
    serializer_class = ZwrotySerialiser
    name = 'zwroty-detail'    