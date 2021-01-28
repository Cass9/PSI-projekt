from django.shortcuts import render
from django.http import HttpResponse
from .serializers import AutoSerializer, KlientSerializer, PrzegladSerializer, UbezpieczenieSerializer, CennikSerializer, WypozyczeniaSerializer, ZwrotySerialiser, UserSerializer
from rest_framework import generics
from rest_framework.reverse import reverse
from .models import Auto, Klient, Przeglad, Ubezpieczenie, Cennik, Wypozyczenia, Zwroty
from rest_framework.response import Response
from django_filters import AllValuesFilter, FilterSet, NumberFilter, DateTimeFilter
from rest_framework import permissions
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    return HttpResponse("Wypożyczalnia samochodów")

class AutoList(generics.ListCreateAPIView):
    queryset = Auto.objects.all()
    serializer_class = AutoSerializer
    filter_fields = ['Marka', 'Model', 'Rok_produkcji', 'moc_silnika']
    search_fields = ['Marka', 'Model']
    name = 'auto-list'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(wlasciciel=self.request.user)

class AutoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Auto.objects.all()
    serializer_class = AutoSerializer
    name = 'auto-detail'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({'auto': reverse(AutoList.name, request=request),
                         'klient': reverse(KlientList.name, request=request),
                         'przeglad': reverse(PrzegladList.name, request=request),
                         'ubezpieczenie':reverse(UbezpieczenieList.name, request=request),
                         'cennik': reverse(CennikList.name, request=request),
                         'wypozyczenia': reverse(WypozyczeniaList.name, request=request),
                         'zwroty':reverse(ZwrotyList.name, request=request),
                        # 'uzytkownicy': reverse(UserList.name, request=request)
                         })
       


class KlientList(generics.ListCreateAPIView):
    queryset = Klient.objects.all()
    serializer_class = KlientSerializer
    filter_fields = ['Imie', 'Nazwisko', 'Miejscowosc']
    search_fields = ['Imie', 'Nazwisko', 'Miejscowosc']
    ordering_fields = ['Imie', 'Nazwisko', 'Miejscowosc']
    name = 'klient-list'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(wlasciciel=self.request.user)

class KlientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Klient.objects.all()
    serializer_class = KlientSerializer
    name = 'klient-detail'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class PrzegladFilter(FilterSet):
    od_data_konca_przegladu = DateTimeFilter(field_name='Data_konca_przegladu', lookup_expr='gte')
    do_data_konca_przegladu = DateTimeFilter(field_name='Data_konca_przegladu', lookup_expr='lte')

    class Meta:
        model = Przeglad
        fields = ['od_data_konca_przegladu', 'do_data_konca_przegladu']

class PrzegladList(generics.ListCreateAPIView):
    queryset = Przeglad.objects.all()
    serializer_class = PrzegladSerializer
    filter_class = PrzegladFilter
    name = 'przeglad-list'

class PrzegladDetail(generics.RetrieveDestroyAPIView):
    queryset = Przeglad.objects.all()
    serializer_class = PrzegladSerializer
    name = 'przeglad-detail'


class UbezpieczenieFilter(FilterSet):
    od_data_konca_ubezpieczenia = DateTimeFilter(field_name='Data_konca_ubezpieczenia', lookup_expr='gte')
    do_data_konca_ubezpieczenia = DateTimeFilter(field_name='Data_konca_ubezpieczenia', lookup_expr='lte')

    class Meta:
        model = Ubezpieczenie
        fields = ['auto_id_auta', 'od_data_konca_ubezpieczenia', 'do_data_konca_ubezpieczenia']

class UbezpieczenieList(generics.ListCreateAPIView):
    queryset = Ubezpieczenie.objects.all()
    serializer_class = UbezpieczenieSerializer
    filter_class = UbezpieczenieFilter
    name = 'ubezpieczenie-list'

class UbezpieczenieDetail(generics.RetrieveDestroyAPIView):
    queryset = Ubezpieczenie.objects.all()
    serializer_class = UbezpieczenieSerializer
    name = 'ubezpieczenie-detail'

class CennikFilter(FilterSet):
    min_cena_za_dobe = NumberFilter(field_name='Cena_za_dobe', lookup_expr='gte')
    max_cena_za_dobe = NumberFilter(field_name='Cena_za_dobe', lookup_expr='lte')

    class Meta:
        model = Cennik
        fields = ['min_cena_za_dobe', 'max_cena_za_dobe']
    
class CennikList(generics.ListCreateAPIView):
    queryset = Cennik.objects.all()
    serializer_class = CennikSerializer
    filter_class = CennikFilter
    name = 'cennik-list'

class CennikDetail(generics.RetrieveDestroyAPIView):
    queryset = Cennik.objects.all()
    serializer_class = CennikSerializer
    name = 'cennik-detail'

class WypozyczeniaFilter(FilterSet):
    od_termin_zwrotu = DateTimeFilter(field_name='termin_zwrotu_zwrotu', lookup_expr='gte')
    do_termin_zwrotu = DateTimeFilter(field_name='termin_zwrotu_zwrotu', lookup_expr='lte')

    class Meta:
        model = Wypozyczenia
        fields = ['klient_id_klienta', 'auto_id_auta', 'od_termin_zwrotu', 'do_termin_zwrotu']

class WypozyczeniaList(generics.ListCreateAPIView):
    queryset = Wypozyczenia.objects.all()
    serializer_class = WypozyczeniaSerializer
    filter_class = WypozyczeniaFilter
    name = 'wypozyczenia-list'

class WypozyczeniaDetail(generics.RetrieveDestroyAPIView):
    queryset = Wypozyczenia.objects.all()
    serializer_class = WypozyczeniaSerializer
    name = 'wypozyczenia-detail'

class ZwrotyFilter(FilterSet):
    od_data_zwrotu = DateTimeFilter(field_name='data_zwrotu', lookup_expr='gte')
    do_data_zwrotu = DateTimeFilter(field_name='data_zwrotu', lookup_expr='lte')

    class Meta:
        model = Zwroty
        fields = ['od_data_zwrotu', 'do_data_zwrotu']

class ZwrotyList(generics.ListCreateAPIView):
    queryset = Zwroty.objects.all()
    serializer_class = ZwrotySerialiser
    filter_class = ZwrotyFilter
    name = 'zwroty-list'

class ZwrotyDetail(generics.RetrieveDestroyAPIView):
    queryset = Zwroty.objects.all()
    serializer_class = ZwrotySerialiser
    name = 'zwroty-detail'    

class UserList(generics.ListAPIView):
        queryset = User.objects.all()
        serializer_class = UserSerializer
        name = 'user-list'

class UserDetail(generics.RetrieveAPIView):
        queryset = User.objects.all()
        serializer_class = UserSerializer
        name = 'user-detail'        