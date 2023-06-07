from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.decorators import api_view
from rest_framework.exceptions import APIException
from .serializers import ParkingSerializer

from .models import parking


@api_view(['GET'])
def getParking(request):
    parkeo = parking.objects.all()
    serializer = ParkingSerializer(parkeo, many = True)
    return Response(serializer.data)


@api_view(['POST'])
def postParking(request):
    data = request.data
    parkeo = parking.objects.create(
        lugar = data['lugar'],
        tiempo = data['tiempo']
    )
        
    serializer = ParkingSerializer(parkeo, many = False)
    return Response(serializer.data)
