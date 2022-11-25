from rest_framework import serializers
from reservas.models import Reservation
from rest_framework.validators import ValidationError

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'
        
    def validate(self, value):
        check_in = value.get("check_in")
        check_out = value.get("check_out")

        if check_in > check_out:
            raise ValidationError("You can't set check-in after check-out")