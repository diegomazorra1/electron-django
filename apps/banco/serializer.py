from rest_framework.serializers import ModelSerializer
from apps.banco.models import Transaccion



class BancoSerializer(ModelSerializer):

    class Meta:
        model = Transaccion
        fields =   "__all__" #('first_name', 'email', )
