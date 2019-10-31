from django.shortcuts import render
import serial
import psycopg2
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.Rfid.form import actualizar_saldo
from django.views.generic import ListView, TemplateView, UpdateView, CreateView
from apps.banco.models import Transaccion
from apps.usuarios.models import Usuario
from django.utils import timezone
import time
from apps.Rfid.models import Global
from apps.Rfid.form1 import SetForm
#from django_cron import CronJobBase, Schedule
import datetime
import logging
from django.db.models import Q
#DEFAULT_LOCK_BACKEND = 'django_cron.backends.lock.cache.CacheLock'
#logger = logging.getLogger('django_cron')


# Create your views here.

#def my_scheduled_job():
    #usuarios= Usuario.objects.filter(sancion=True).update(sancion=False)

"""
#class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 2
    MIN_NUM_FAILURES = 3

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)

    #RUN_AT_TIMES = ['00:50', '18:50', '00:25']
    #schedule = Schedule(run_at_times=RUN_AT_TIMES)
    code = 'apps.my_cron_job'

    def do(self):
        usuarios= Usuario.objects.filter(sancion=True).update(sancion=False)"""



def inicioRfid(request):
    return render(request, 'rfid/identificador_rfid.html')

def inicioAutorizar(request):

    return render(request, 'rfid/identificador_autorizacion.html')


def retornar(request):
    """
    global usuario2
    global request
    ss = True
    if ss ==  True:
        """
    return   render(request,'rfid/busqueda_rfid.html', {'usuario2':usuario2, 'usuari':True   } )


def LecturaUid(request):










    # conexion a la base de datos-----------

    try:
      #conn_string="dbname='SASRU' user='postgres' host='localhost' password='ingenieria@'
      #arduino = serial.Serial('COM8',9600, timeout=.1)


      #conn = psycopg2.connect(conn_string)
      print ("connection succeeded")
    except:

        serial.Serial('COM8',9600, timeout=.1).close()
        #print ("no connection to db")

    #cur = conn.cursor()




    #---------------------------------------------------------





    bandera=1
    arduino = serial.Serial('COM8',9600, timeout=.1)





    while 1 :

            #ELIMNAR CARACTERES DE NUEVA LINEA DE Serial.println de Arduino

            data = arduino.readline()[:-2]
            data = data.decode("utf-8")

    ##        print(data)

            if data:
                """
                print (data)
                print (type(data))
                print (len(data))
                """
                if 'UID' in data:
                        UID = data[4:]
                        print ("llego el identificador", UID)

                if 'Name' in data:
                        Nombre = data[5:]
                        print ("llego el Nombre", Nombre)
                if 'Saldo' in data:
                        Saldo = data[7:]
                        print ("llego el SALDO", Saldo )
                        print (type(Saldo))


                        Saldo_str = str(Saldo)

                        print(UID)
                        print (type(UID))
                        usuario2= Usuario.objects.filter(uid=UID)


                        bandera= 0


                        print(usuario2)
                        return   render(request,'rfid/busqueda_rfid.html', {'usuario2':usuario2, 'usuari':True   } )



            else:
                print ("no hay datos")





    #conn.close()

    #return redirect('rfid:index3')


class Actualizar_Saldo(UpdateView):


    model= Usuario
    form_class= actualizar_saldo
    template_name='rfid/Saldo_form.html'
    success_url= reverse_lazy('rfid:inicio')




def autorizar(request):







    now= datetime.datetime.now()
    hora_act=now.time()

    H1_des = datetime.time(7, 0, 0, 0)
    H2_des = datetime.time(11, 40, 0, 0)
    H1_alm = datetime.time(11, 30, 0, 0)
    H2_alm = datetime.time(13, 55, 0, 0)
    H1_cen = datetime.time(16, 00, 0, 0)
    H2_cen = datetime.time(23, 50, 0, 0)


    def Act_servicio(servicio_actual,id_usuario):
        # modificar la casilla de reseva en la base de datos
        if servicio_actual == "D":

            rank=Usuario.objects.get(id=id_usuario)
            rank.reserva_desayuno= False
            rank.save()

            #transaccion=Transaccion.objects.update(persona_id_id=id_usuario, Valor_de_transaccion=1, tipo_de_transaccion=2,codigo=rank.codigo)



        elif servicio_actual == "A" :
            rank=Usuario.objects.get(id=id_usuario)
            rank.reserva_desayuno= False
            rank.save()





    def servicio(hora_act,D,A,C):
        servicio  = False
        Act_servicio= False
        comida = ""
        print(hora_act)

        print("hola")
        # aca se verificara si el servicio esta habilitado
        if hora_act > H1_des and hora_act < H2_des:
            print("desayuno")

            comida = "Desayuno"
            if D == True:
                servicio = True
                servicio_actual= "D"
                #Act_servicio(servicio_actual)

            else:
                servicio = False

        elif hora_act > H1_alm and hora_act < H2_alm:
            print("almuerzo")
            comida = "Almuerzo"
            if A == True:
                servicio = True
                servicio_actual = 1
                #Act_servicio(servicio_actual)

            else:
                servicio = False



        elif hora_act > H1_cen and hora_act < H2_cen:
            comida = "Cena"
            print("chao")
            if C == True:

                servicio = True
                servicio_actual= "C"



            else:
                servicio = False





        return servicio, comida











    #---------------------------------------------------------

    # Realizar query a database / UID

    try:
      conn_string="dbname='SASRU' user='postgres' host='localhost' password='ingenieria@'"
      print ("Connecting to database\n->%s" % (conn_string))

      conn = psycopg2.connect(conn_string)
      print ("connection succeeded")
    except:
      print ("no connection to db")

    cur = conn.cursor()




    #---------------------------------------------------------




    arduino = serial.Serial('COM8',9600, timeout=.1)


    while True:
            #ELIMNAR CARACTERES DE NUEVA LINEA DE Serial.println de Arduino

            data = arduino.readline()[:-2]
            data = data.decode("utf-8")
    ##        print(data)

            if data:
                """
                print (data)
                print (type(data))
                print (len(data))
                """
                if 'UID' in data:
                        UID = data[4:]
                        print ("llego el identificador", UID)



                if 'Name' in data:
                        Nombre = data[5:]
                        print ("llego el Nombre", Nombre)
                if 'Saldo' in data:
                        Saldo = data[7:]
                        print ("llego el SALDO", Saldo )
                        print (type(Saldo))


                        Saldo_str = str(Saldo)

                        print(UID)

                        validacion1 = Usuario.objects.filter(uid=UID).exists()

                        if validacion1 is False:
                            print("No es valida la tarjeta")
                            nombre_servicio="por ahora"


                            return   render(request,'rfid/autorizacion.html',  {'nombre_servicio':nombre_servicio, 'resulta':True    })

                        else:

                            user=Usuario.objects.get(uid=UID)
                            user1=Usuario.objects.filter(uid=UID)

                            D = user.reserva_desayuno
                            A = user.reserva_almuerzo
                            C = user.reserva_cena

                            print("Reserva Desayuno: ", D)
                            print("Reserva Almuerzo: ", A)
                            print("Reserva Comida: ", C)




                            result, nombre_servicio = servicio(hora_act,D,A,C)

                            print(result)
                            print(result)
                            print(nombre_servicio)
                            print(user1)



                            if(result == True):
                                print("Tiene servicio", nombre_servicio)
                            else:
                                print("NO tiene servicio",nombre_servicio)







                        return   render(request,'rfid/autorizacion.html',  {'nombre_servicio':nombre_servicio, 'user1':user1, 'result':result   })



            else:
                print ("no hay datos")






    conn.close()






def descuento_autorizacion(request,id_usuario):


    now= datetime.datetime.now()
    hora_act=now.time()
    fecha_act= now.date()

    H1_des = datetime.time(7, 0, 0, 0)
    H2_des = datetime.time(11, 40, 0, 0)
    H1_alm = datetime.time(11, 30, 0, 0)
    H2_alm = datetime.time(13, 55, 0, 0)
    H1_cen = datetime.time(16, 00, 0, 0)
    H2_cen = datetime.time(23, 50, 0, 0)

    rank=Usuario.objects.get(id=id_usuario)
    rank.comida_consumida= True
    rank.sancion= True


    rank.save()

    transaccion=Transaccion.objects.create(persona_id_id=id_usuario, Valor_de_transaccion=1100, tipo_de_transaccion=2,codigo=rank.codigo)
    cuposedit=Global.objects.get(fecha_de_transaccion=fecha_act)





    if  hora_act > H1_des and hora_act < H2_des:

        cuposedit.cupos_disponibles-=1
        #cuposedit.cupos_desayuno-=1
        cuposedit.save()

        rank=Usuario.objects.get(id=id_usuario)
        rank.reserva_desayuno= False

        rank.save()


        #transaccion=Transaccion.objects.update(persona_id_id=id_usuario, Valor_de_transaccion=1, tipo_de_transaccion=2,codigo=rank.codigo)



    elif  hora_act > H1_alm and hora_act < H2_alm:
        rank=Usuario.objects.get(id=id_usuario)
        rank.reserva_almuerzo= False
        rank.save()
        cuposedit.cupos_disponibles-=1
        #cuposedit.cupos_vendidos+=1
        #cuposedit.cupos_almuerzo-=1
        cuposedit.save()


        #if rank.reserva_desayuno == True:
            #rank.sancion = True
            #rank.save()




    elif hora_act > H1_cen and hora_act < H2_cen:
        rank=Usuario.objects.get(id=id_usuario)
        rank.reserva_cena= False
        rank.save()
        cuposedit.cupos_disponibles-=1
        #cuposedit.cupos_cena-=1
        cuposedit.save()
        #if rank.reserva_almuerzo == True:
        #    rank.sancion = True
        #    rank.save()









    return   render(request,'rfid/autorizacion.html')




class CuposCreate(CreateView):
	model = Global
	form_class = SetForm
	template_name = 'banco/inicio.html'
	success_url = reverse_lazy('banco:setpoint1')

def mostrar(request):
    now= datetime.datetime.now()
    fecha_act=now.date()
    validacion1 = Global.objects.filter(fecha_de_transaccion=fecha_act).exists()

    if validacion1==True:


        return render(request, 'banco/inicio.html', {'validacion': False })

    else:
        if request.method == 'POST' :
            form= SetForm(request.POST)

            if form.is_valid():

                form.save()

            return redirect('rfid:vista_cupos')
        else:
            form= SetForm()


        return render(request, 'banco/inicio.html', {'form':form })









#$def vistacupos(request):
    #usuario2 = Usuario.objects.all()
    #contexto = {'usuario2': usuario2}
    #return render(request, 'banco/inicio2.html', contexto)

def vistacupos(request):
    print("HOLAAA")


    now= datetime.datetime.now()
    hora_act=now.time()

    H1_des = datetime.time(7, 0, 0, 0)
    H2_des = datetime.time(11, 40, 0, 0)
    H1_alm = datetime.time(12, 30, 0, 0)
    H2_alm = datetime.time(13, 55, 0, 0)
    H1_cen = datetime.time(16, 00, 0, 0)
    H2_cen = datetime.time(23, 50, 0, 0)


    if  hora_act > H1_des and hora_act < H2_des:

        servicio ="desayuno"
        print("Hola")





    elif  hora_act > H1_alm and hora_act < H2_alm:
        servicio = "almuerzo"




    elif hora_act > H1_cen and hora_act < H2_cen:
        servicio = "cena"
    else:
        print("no es horario")
        servicio= "No es horario"


    usuario2 = Global.objects.all()



    return render(request, 'rfid/cupos.html', {'H1_des':H1_des,'servicio':servicio,'H2_des':H2_des,'H1_alm':H1_alm,'H2_alm':H2_alm,'H1_cen':H1_cen,'H2_cen':H2_cen,'hora_act':hora_act,'usuario2':usuario2})

def prueba(request):


    busquedatotal=Usuario.objects.all()

    for consumo in busquedatotal.iterator():
        consumo.comida_consumida=False
        consumo.sancion=False
        consumo.save()



    now= datetime.datetime.now()
    hora_act=now.time()
    fecha_act=now.date()

    H1_des = datetime.time(7, 0, 0, 0)
    H2_des = datetime.time(11, 40, 0, 0)
    H1_alm = datetime.time(12, 30, 0, 0)
    H2_alm = datetime.time(13, 55, 0, 0)
    H1_cen = datetime.time(16, 00, 0, 0)
    H2_cen = datetime.time(23, 50, 0, 0)


    if  hora_act > H1_des and hora_act < H2_des:

        busqueda1 = Q(reserva_desayuno=True)
        opcion='d'









    elif  hora_act > H1_alm and hora_act < H2_alm:
        busqueda1 = Q(reserva_almuerzo=True)
        opcion='a'




    elif hora_act > H1_cen and hora_act < H2_cen:
        busqueda1 = Q(reserva_cena=True)
        opcion='c'

    else:
        pass



    busqueda=Usuario.objects.filter(busqueda1 )
    i=0

    #busqueda=Usuario.objects.filter(busqueda1 | busqueda2 )


    for mod in busqueda.iterator():

        id_usuario=mod.id
        print(id_usuario)

        rank=Usuario.objects.get(id=id_usuario)
        rank.comida_consumida=False
        rank.sancion=False
        transaccion=Transaccion.objects.create(persona_id_id=id_usuario, Valor_de_transaccion=1100, tipo_de_transaccion=2,codigo=rank.codigo)
        print(busqueda.iterator())
        i+=1

        if opcion =='d':
            mod.reserva_desayuno=False
            mod.save()
        elif opcion =='a':
            mod.reserva_almuerzo=False
            mod.save()
        elif opcion =='c':
            mod.reserva_cena=False
            mod.save()



        print(i)
        print (type(i))
    reservas=Global.objects.get(fecha_de_transaccion=fecha_act)
    print(reservas)
    reservas.reservas_no_redimidas+=i
    reservas.save()
    usuario2=Global.objects.all()
    print(opcion)

    return render(request, 'rfid/cupos2.html', {'i':i,'opcion':opcion,'usuario2':usuario2})














        #print(Usuario.objects.filter(sancion=True))


        #transaccion=Transaccion.objects.create(persona_id_id=mod.id, Valor_de_transaccion=1100, tipo_de_transaccion=2,codigo=mod.codigo)
