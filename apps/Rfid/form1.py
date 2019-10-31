from django import forms
from apps.Rfid.models import Global



class SetForm(forms.ModelForm):

    class Meta:
        model = Global




        fields = [

        'cupos_totales',
        'cupos_desayuno',
        'cupos_almuerzo',
        'cupos_cena',

        ]
        labels = {
        'cupos_totales':    ' Numero de cupos totales',
        'cupos_desayuno':    ' Numero de desayunos del dia',
        'cupos_almuerzo':   ' Numero de almuerzos del dia',
        'cupos_cena':       ' Numero de cenas del dia',

        }
        widgets= {
        'cupos_totales' :             forms.TextInput(attrs= {'class': 'form-control'}  ),
        'cupos_desayuno' :            forms.TextInput(attrs= {'class': 'form-control'}  ),
        'cupos_almuerzo':             forms.TextInput(attrs= {'class': 'form-control'}  ),
        'cupos_cena' :                forms.TextInput(attrs= {'class': 'form-control'}  ),




        }
