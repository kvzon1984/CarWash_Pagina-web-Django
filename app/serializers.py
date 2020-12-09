
from .models  import Insumo, Contacto
from rest_framework import serializers



class InsumoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insumo
        fields =  '__all__'




class ContactoSerializer(serializers.ModelSerializer):

    class Meta:

        model = Contacto
        fields = '__all__'