from .serializers import AdsSerializer
from rest_framework import generics
from anuncios.models import Ad


class AdsAPIView(generics.ListCreateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdsSerializer


class AdAPIView(generics.RetrieveUpdateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdsSerializer
