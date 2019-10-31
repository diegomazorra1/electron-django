from django import forms
from apps.banco.models import Transaccion





class TransaccionForm(forms.ModelForm):

    class Meta:
        model = Transaccion

        fields = [
        'persona_id',
        'tipo_de_transaccion',
        'codigo' ,
        'Valor_de_transaccion' ,
        ]
        labels = {
        'persona_id' :             'ID de persona',
        'tipo_de_transaccion':     'Tipo de transaccion',
        'codigo' :                    'Codigo estudiante',
        'Valor_de_transaccion' :   'Valor ',
        }
        widgets= {
        'persona_id' :                forms.Select(attrs= {'class': 'form-control'}  )      ,
        'tipo_de_transaccion':        forms.Select(attrs= {'class': 'form-control'}  )      ,
        'codigo' :                       forms.TextInput(attrs= {'class': 'form-control'}  ),
        'Valor_de_transaccion' :      forms.TextInput(attrs= {'class': 'form-control'}  )  ,



        }
