from django.urls import path, include
from django.contrib import admin
from apps.Rfid.views import CuposCreate, mostrar , vistacupos
from apps.banco.views import index, banco_view,Bancolist, BuscarView, index_1, search, lista_transacciones, BuscarRecarga
from django.contrib.auth.decorators import login_required


app_name = 'variable12'
urlpatterns = [
    path('', index,name='index'),
    path('nuevo/',login_required (banco_view), name='banco_crear'),
    path('nuevo/lista', login_required (Bancolist.as_view()), name='banco_lista'),
    path('nuevo/busquedas/', login_required ( BuscarView.as_view()),name='buscarlo'),
    path('n', index_1,name='index_usuarios'),
    path('busqueda', search,name='search'),
    path('listasapi',  lista_transacciones,name='api'),
    #path('inicio',  login_required(CuposCreate.as_view()),name='setpoint'),
    path('inicio2',  login_required(mostrar),name='setpoint1'),
    path('inicio3',  login_required(vistacupos),name='setpointview'),
    path('nuevo/busquedas1/', login_required ( BuscarRecarga.as_view()),name='buscar_recarga'),




]
