from django.urls import path
from . import views 

urlpatterns = [
    
    path('auto', views.AutoList.as_view(),name=views.AutoList.name),
    path('auto/<int:pk>', views.AutoDetail.as_view(),name=views.AutoDetail.name),
    path('klient', views.KlientList.as_view(),name=views.KlientList.name),
    path('klient/<int:pk>', views.KlientDetail.as_view(),name=views.KlientDetail.name),
    path('przeglad', views.PrzegladList.as_view(),name=views.PrzegladList.name),
    path('przeglad/<int:pk>', views.PrzegladDetail.as_view(),name=views.PrzegladDetail.name),
    path('ubezpieczenie', views.UbezpieczenieList.as_view(),name=views.UbezpieczenieList.name),
    path('ubezpieczenie/<int:pk>', views.UbezpieczenieDetail.as_view(),name=views.UbezpieczenieDetail.name),
    path('cennik', views.CennikList.as_view(),name=views.CennikList.name),
    path('cennik/<int:pk>', views.CennikDetail.as_view(),name=views.CennikDetail.name),
    path('wypozyczenia', views.WypozyczeniaList.as_view(),name=views.WypozyczeniaList.name),
    path('wypozyczenia/<int:pk>', views.WypozyczeniaDetail.as_view(),name=views.WypozyczeniaDetail.name),
    path('zwroty', views.ZwrotyList.as_view(),name=views.ZwrotyList.name),
    path('zwroty/<int:pk>', views.ZwrotyDetail.as_view(),name=views.ZwrotyDetail.name),
    #path('users', views.UserList.as_view(), name=views.UserList.name),
    #path('users/<int: pk>', views.UserDetail.as_view(), name=views.UserDetail.name),
    path('', views.ApiRoot.as_view(), name=views.ApiRoot.name),
]
