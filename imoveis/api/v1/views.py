from .serializers import PropertiesSerializer
from rest_framework import viewsets
from imoveis.models import Propertie


class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Propertie.objects.all()
    serializer_class = PropertiesSerializer
