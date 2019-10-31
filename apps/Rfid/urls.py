from django.urls import path, include
from django.contrib import admin
from apps.Rfid.views import LecturaUid, inicioRfid, Actualizar_Saldo, autorizar, inicioAutorizar, descuento_autorizacion, prueba, vistacupos
from django.contrib.auth.decorators import login_required


app_name = 'variable123'



urlpatterns = [
path('inicio/lectura/', login_required (LecturaUid),name='index3'),
path('inicio/',login_required ( inicioRfid),name='inicio'),
path('editar/<int:pk>/',login_required(Actualizar_Saldo.as_view()),name='saldo_editar'),
path('inicio/',login_required (inicioRfid),name='inicio'),
path('inicio/autorizar',login_required ( inicioAutorizar),name='inicio_autorizar'),
path('Autorizar/', login_required (autorizar),name='autorizacion'),
path('Autorizar/descuento/<int:id_usuario>/',login_required (descuento_autorizacion),name='descuento_autorizacion'),
path('prueba/', login_required (vistacupos),name='vista_cupos'),
path('redimir/',login_required (prueba) ,name='redimir'),







]
