from django.db import models

# Create your models here.

class Global(models.Model):
    cupos_totales= models.IntegerField(default=0)
    cupos_desayuno = models.IntegerField(default=0)
    cupos_almuerzo = models.IntegerField(default=0)
    cupos_cena = models.IntegerField(default=0)
    cupos_disponibles =  models.IntegerField(default=0)
    cupos_vendidos = models.IntegerField(default=0, editable = False)
    fecha_de_transaccion= models.DateField ( auto_now = False , auto_now_add = True )
    reservas_no_redimidas= models.IntegerField(default=0)


    def save(self,*args, **kwargs):

        if self.cupos_totales<=self.cupos_desayuno+self.cupos_almuerzo+self.cupos_cena:
            self.cupos_disponibles=self.cupos_totales

        return super(Global, self).save( *args, **kwargs)


    def __str__(self):
        return '{} '.format( self.fecha_de_transaccion)
