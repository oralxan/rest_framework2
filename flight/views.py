from django.shortcuts import render
from django.http import JsonResponse
from .models import Flight
from .serializer import FlightSerialializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

def flight_page(request):
    context = {
        '5i':'world'
    }
    return JsonResponse(context)
@api_view(['GET','POST'])
def flightss(request):
    if request.method == 'GET':
        flight2 = Flight.objects.all()
        serializer = FlightSerialializer(flight2, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = FlightSerialializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
  

@api_view(['GET','PUT','DELETE'])
def flight_detail(request,pk):
    try:
        flight = Flight.objects.get(pk=pk)
    except Flight.DoesNotExist:
        return Response(
            status= status.HTTP_404_NOT_FOUND
        )
    if request.method == 'GET':
        serializer = FlightSerialializer(flight)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )
    if request.method == 'PUT':
        serializer = FlightSerialializer(flight, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status= status.HTTP_202_ACCEPTED

            )
        return Response(
            serializer.errors,
            status=status.HTTP_406_NOT_ACCEPTABLE
        )
    elif request.method == 'DELETE':
        flight.delete()
        return Response(
            'Delete successfully',
            status=status.HTTP_202_ACCEPTED

        )

