from rest_framework import serializers
from imoveis.models import Propertie

class PropertiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Propertie
        fields = '__all__'