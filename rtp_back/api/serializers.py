from rest_framework.serializers import ModelSerializer
from .models import parking


class ParkingSerializer(ModelSerializer):
    class Meta:
        model = parking
        fields = '__all__'