from django import forms
from apps.usuarios.models import Usuario





class actualizar_saldo(forms.ModelForm):

    class Meta:
        model = Usuario

        fields = [
        'saldo',
        'reserva_desayuno',
        'reserva_almuerzo',
        'reserva_cena',



        ]
        labels = {
        'saldo':               'Saldo',
        'reserva_desayuno':    'Compra Desayuno',
        'reserva_almuerzo':    'Compra Almuerzo',
        'reserva_cena':        'Compra Cena',


        }
        widgets= {
        'saldo':              forms.TextInput(attrs= {'class': 'form-control'}  ),
        'reserva_desayuno':  forms.CheckboxInput(attrs= {'class': 'form-control'}  ),
        'reserva_almuerzo' : forms.CheckboxInput(attrs= {'class': 'form-control'}  ),
        'reserva_cena' :     forms.CheckboxInput(attrs= {'class': 'form-control'}  ),





        }
