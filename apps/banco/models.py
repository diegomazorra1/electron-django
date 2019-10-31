from django.db import models
from apps.usuarios.models import Usuario
from django.db.models.signals import post_save
from django.shortcuts import render, redirect
from apps.Rfid.models import Global
import datetime
import time



# Create your models here.

class Transaccion(models.Model):

    transacciones=((1,'Recarga'),(2,'Compra'))
    persona_id = models.ForeignKey(Usuario, related_name='+', null=True, blank=False, on_delete=models.CASCADE)
    tipo_de_transaccion=models.IntegerField(choices=transacciones,default=1)
    codigo = models.CharField(max_length=11)
    Valor_de_transaccion= models.IntegerField()
    fecha_de_transaccion= models.DateTimeField ( auto_now = False , auto_now_add = True )

    def save(self,*args, **kwargs):
        #rank=Usuario.objects.update(saldo=self.Valor_de_transaccion)
        rank1=Usuario.objects.get(id=self.persona_id_id)
        if self.tipo_de_transaccion==1:
            rank1.saldo+=self.Valor_de_transaccion
            rank1.save()
            print("suma saldo")
        else :
            now= datetime.datetime.now()
            fecha_act= now.date()
            cuposedit=Global.objects.get(fecha_de_transaccion=fecha_act)
            cuposedit.cupos_vendidos+=1
            cuposedit.save()

            rank1.saldo-=self.Valor_de_transaccion
            rank1.save()
            print("desconto uno")


        return super(Transaccion, self).save( *args, **kwargs)




    def __str__(self):
        return '{} {} {}'.format(self.persona_id.nombre, self.codigo, self.fecha_de_transaccion)





"""def edit_saldo(sender,**kwargs):
    if kwargs['created']:
        edit = Usuario.objects.update(saldo=Valor_de_transaccion)

post_save.connect(edit_saldo, sender=Transaccion)"""
