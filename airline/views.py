from django.shortcuts import render
from django.http import JsonResponse
from .models import Airline
from .serializer import AirlineSerialializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

def home_page(request):
    context = {
        'hk':'world'
    }
    return JsonResponse(context)
@api_view(['GET','POST'])
def airliness(request):
    if request.method == 'GET':
        airlines2 = Airline.objects.all()
        serializer = AirlineSerialializer(airlines2, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = AirlineSerialializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
  

@api_view(['GET','PUT','DELETE'])
def airline_detail(request,pk):
    try:
        airline = Airline.objects.get(pk=pk)
    except Airline.DoesNotExist:
        return Response(
            status= status.HTTP_404_NOT_FOUND
        )
    if request.method == 'GET':
        serializer = AirlineSerialializer(airline)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )
    if request.method == 'PUT':
        serializer = AirlineSerialializer(airline, data=request.data)
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
        airline.delete()
        return Response(
            'Delete successfully',
            status=status.HTTP_202_ACCEPTED

        )

