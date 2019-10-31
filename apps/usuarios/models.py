from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Usuario(models.Model):


    nombre = models.CharField(max_length=15 )
    apellidos = models.CharField(max_length=20)
    foto = models.ImageField(upload_to='photos', null= True, blank = True)
    cedula = models.CharField(max_length=12)
    codigo = models.CharField(max_length=11)
    programa = models.CharField(max_length=25)
    uid = models.CharField(max_length=20)
    email = models.EmailField()
    saldo = models.PositiveIntegerField(null=False, blank=True,default=0)
    reserva_desayuno= models.BooleanField(default=False)
    reserva_almuerzo= models.BooleanField(default=False)
    reserva_cena= models.BooleanField(default=False)
    sancion= models.BooleanField(default=False)
    comida_consumida=models.BooleanField(default=False)



    def __str__(self):
        return '{} {} {}'.format(self.apellidos, self.nombre, self.uid)


#class Tipo_de_transaccion(models.Model):

        #tipo = models.CharField(max_length=50)


        #def __str__(self):
                #return '{} '.format(self.tipo)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='profiles', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    link = models.URLField(max_length=200, null=True, blank=True)

    class Meta:
        ordering = ['user__username']
