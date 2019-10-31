from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.banco.form import TransaccionForm
from django.views.generic import ListView, TemplateView, CreateView
from apps.banco.models import Transaccion
from apps.usuarios.models import Usuario
import psycopg2
import datetime
import time
from datetime import datetime
import json
from django.core import serializers
# Create your views here.

def index(request):
    return render(request, 'banco/index.html')


def index_1(request):
    return   render(request,'prueba/prueba.html' )



def banco_view(request):
    if request.method == 'POST' :
        form= TransaccionForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('banco:index')
    else:
        form= TransaccionForm()
    return render(request, 'banco/banco_form.html', {'form':form })


class Bancolist(ListView):
    object_list = Transaccion.objects.all().order_by('id')
    model= Transaccion
    template_name= 'banco/banco_list.html'


class BuscarView(TemplateView):
    def post(self, request, *args, **kwargs):
        buscar= request.POST['buscalo']
        transacciones= Transaccion.objects.filter(codigo__contains=buscar)
        usuarios= Usuario.objects.filter(cedula__contains=buscar)

        if transacciones:

            datos= []
            for transaccion in transacciones:
                usuarios= transaccion.persona_id
                datos.append(dict([(transaccion,usuarios)]))
                print (datos)
                print('1')
            return   render(request,'busquedas/buscar.html',
                       {'datos':datos} )


        else:

            print('chao')

            return   render(request,'busquedas/buscar.html' )

def search(request):
    title= request.GET.get('title') #diccionario
    #select * from videos where title= 'first'
    busqueda= Transaccion.objects.filter(codigo=title)
    busqueda= [ busqueda_serializer(busquedas) for busquedas in busqueda  ] #lista de diccionarios
    return HttpResponse(json.dumps(busqueda), content_type= 'application/json')

def busqueda_serializer(busquedas):
    return { 'id':busquedas.id  }

def lista_transacciones(request):


    lista= serializers.serialize('json', Transaccion.objects.all())

    return HttpResponse(lista, content_type='application/json')



class BuscarRecarga(TemplateView):
    def post(self, request, *args, **kwargs):
        buscar= request.POST['buscalo']
        usuario2= Usuario.objects.filter(codigo=buscar)
        if usuario2:
            return   render(request,'banco/busqueda_recarga.html', {'usuario2':usuario2, 'usuari':True   } )





        else:

            return   render(request,'busquedas/buscar.html' )
