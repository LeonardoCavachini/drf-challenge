from .serializers import ReservationSerializer
from rest_framework import mixins
from rest_framework import viewsets
from reservas.models import Reservation


class ReservationsViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet):
    
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer