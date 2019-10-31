from django.shortcuts import render, redirect
from django.template import RequestContext
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from apps.usuarios.models import Usuario
from apps.banco.models import Transaccion
from django import forms
from django.urls import reverse_lazy
from apps.usuarios.form import usuarios_form, ProfileForm
#from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from apps.usuarios.forms_user import RegistroForm
from apps.banco.form import TransaccionForm
from .models import Profile
from django.core import serializers
import json
#from rest_framework.views import APIView
#from apps.usuarios.serializer import UserSerializer





# Create your views here.

def listadousuarios(request):
    lista=serializers.serialize('json', Usuario.objects.all(), fields= ['username','first_name'])
    return HttpResponse(lista, content_type='application/json')




def index_usuarios(request):
    return HttpResponse("SOY LA PAGINA PRINCIPAL DE LA APLICACION")


def index_1(request):
    return   render(request,'pruebas/prueba.html' )



class Usuarioslist(ListView):
    usuario = Usuario.objects.all().order_by('id')

    model= Usuario
    template_name= 'usuarios/usuarios_list.html'

def usuarios_list(request):
    usuario = Usuario.objects.all().order_by('id')
    contexto = {'usuarios': usuario}
    return render(request, 'usuarios/usuarios_list0.html', contexto)


class Usuarios_Crear(CreateView):

    model= Usuario
    form_class= usuarios_form
    template_name='usuarios/usuarios_form.html'
    success_url= reverse_lazy('usuarios:usuario_listas')

def usuario_crear(request):
    #obtener= Usuario()
    if request.method == 'POST' :
        form= usuarios_form(request.POST, request.FILES)
        #obtener.foto = request.FILES.get('txtImagen')
        if form.is_valid():
            form.save()
            #obtener.save()
        return redirect('usuarios:usuario_listas')
    else:
        form= usuarios_form()
    return render(request,'usuarios/usuarios_form.html', {'form':form }      )







class Usuarios_Actualizar(UpdateView):
    model= Usuario
    form_class= usuarios_form
    template_name='usuarios/usuarios_form.html'
    success_url= reverse_lazy('usuarios:usuario_listas')

class Usuarios_Eliminar(DeleteView):
    model= Usuario
    form_class= usuarios_form
    template_name='usuarios/usuarios_delete.html'
    success_url= reverse_lazy('usuarios:usuario_listas')

class RegistroUsuario(CreateView):
	model = User
	template_name = "usuarios/registrar.html"
	form_class = RegistroForm
	success_url = reverse_lazy('usuarios:usuario_listas')



"""
class UserApi(APIView):
	serializer= UserSerializer
	def get (self, request, format=None ):

		lista = User.objects.all()

		response = self.serializer(lista, many=True)

		return HttpResponse(json.dumps(response.data), content_type='application/json')
"""

class BuscarView(TemplateView):
    def post(self, request, *args, **kwargs):
        buscar= request.POST['buscalo']
        usuario2= Usuario.objects.filter(codigo__contains=buscar)
        usuario3= Usuario.objects.filter(cedula__contains=buscar)
        if usuario2:
            print ("ha buscado por su apellido")
            print(usuario2)
            return   render(request,'busquedas/buscar.html', {'usuario2':usuario2, 'usuari':True   } )


        elif usuario3:
            print ("ha buscado por su cedula")
            print(usuario3)
            return   render(request,'busquedas/buscar.html', {'usuario2':usuario3, 'usuari':True   } )




        else:

            return   render(request,'busquedas/buscar.html' )

def crear_trans(request,id_usuario):

    user = Transaccion.objects.filter(persona_id_id=id_usuario).exists()
    print(user)
#____





#____________________
    if user == False:
        rank=Usuario.objects.get(id=id_usuario)




        transaccion=Transaccion.objects.create(persona_id_id=id_usuario, Valor_de_transaccion=0)
        transaccion.codigo=rank.codigo
        transaccion.save()
    else:
        print(user)
        print(user)

    mascota = Transaccion.objects.filter(persona_id_id=id_usuario).first()


    if request.method == 'POST':
        form = TransaccionForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('banco:banco_lista')
    else :
        form = TransaccionForm(instance=mascota)
    return render(request, 'usuarios/usuarios_form.html', {'form': form })


class Ilogin(TemplateView):
    template_name='login/login.html'
    success_url= reverse_lazy('usuarios:usuario_listas')



@method_decorator(login_required, name='dispatch')
class ProfileUpdate(LoginRequiredMixin,UpdateView):
    model= Profile
    form_class= ProfileForm
    #fields=['avatar', 'bio', 'link']
    success_url= reverse_lazy('usuarios:profile')
    template_name= 'registration/profile_form.html'

    def get_object(self):
        #recuperar el objeto a editar
        profile, created= Profile.objects.get_or_create(user=self.request.user)
        return profile
