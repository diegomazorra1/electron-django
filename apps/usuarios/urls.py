from django.urls import path, include
from django.contrib import admin
from apps.usuarios.views import index_usuarios, Usuarioslist, Usuarios_Crear, Usuarios_Actualizar, Usuarios_Eliminar, RegistroUsuario, usuarios_list, listadousuarios,BuscarView, \
crear_trans, usuario_crear, Ilogin, ProfileUpdate
from django.contrib.auth.decorators import login_required


app_name = 'variable3'
urlpatterns = [


    #path('', index_usuarios,name='index_usuarios'),
    path('nuevo/lista', login_required( usuarios_list),name='usuario_listas'),
    #path('nuevo', login_required(Usuarios_Crear.as_view()),name='usuario_crear'),
    path('nuevo', login_required(usuario_crear),name='usuario_crear'),
    path('editar/<int:pk>/',login_required(Usuarios_Actualizar.as_view()),name='usuario_editar'),
    path('eliminar/<int:pk>/',login_required( Usuarios_Eliminar.as_view()),name='usuario_eliminar'),
    path('registro/nuevo', RegistroUsuario.as_view(),name='usuario_registro'),
    path('listao', listadousuarios,name='index_list'),
    #path('Api', UserApi.as_view(),name='api'),
    path('nuevo/busquedas/',  BuscarView.as_view(),name='buscarlo'),
    path('transaccion/<int:id_usuario>/', crear_trans,name='crear_trans'),


    path('profile/', ProfileUpdate.as_view(), name="profile" ),




]
