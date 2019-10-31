from django import forms
from apps.usuarios.models import Usuario, Profile





class usuarios_form(forms.ModelForm):

    class Meta:
        model = Usuario

        fields = [
        'nombre',
        'apellidos',
        'cedula' ,
        'codigo',
        'programa' ,
        'uid',
        'email' ,
        #'foto' ,


        ]
        labels = {
        'nombre':     'Nombre',
        'apellidos':  'Apellidos',
        'cedula' :    'Cedula',
        'codigo' :    'Codigo',
        'programa':   'Progama',
        'uid':        'Uid',
        'email' :     'Email',
        #'foto' :     'Foto',

        }
        widgets= {
        'nombre':     forms.TextInput( attrs= {'class': 'form-control'}  ),
        'apellidos':  forms.TextInput(attrs= {'class': 'form-control'}  ),
        'cedula' :    forms.TextInput(attrs= {'class': 'form-control'}  ),
        'codigo' :    forms.TextInput(attrs= {'class': 'form-control'}  ),
        'programa':   forms.TextInput(attrs= {'class': 'form-control'}  ),
        'uid':        forms.TextInput(attrs= {'class': 'form-control'}  ),
        'email' :     forms.TextInput(attrs= {'class': 'form-control'}  ),
        #'foto' :      forms.FileInput(attrs= {'class': 'form-control'}  ),





        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile

        fields = [
        'avatar',
        'bio' ,
        'link',



        ]
        labels = {
        'avatar': 'Avatar',
        'bio' :    'Bio',
        'link':   'Link',


        }
