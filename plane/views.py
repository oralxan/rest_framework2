from django.shortcuts import render
from django.http import JsonResponse
from .models import Plane
from .serializer import PlaneSerialializer
from rest_framework import  status
from rest_framework.decorators import api_view
from rest_framework.response import Response

def plane_page(request):
    context = {
        'hi':'world'
    }
    return JsonResponse(context)
@api_view(['GET','POST'])
def planess(request):
    if request.method == 'GET':
        plane2 = Plane.objects.all()
        serializer = PlaneSerialializer(plane2, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = PlaneSerialializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
  

@api_view(['GET','PUT','DELETE'])
def plane_detail(request,pk):
    try:
        plane = Plane.objects.get(pk=pk)
    except Plane.DoesNotExist:
        return Response(
            status= status.HTTP_404_NOT_FOUND
        )
    if request.method == 'GET':
        serializer = PlaneSerialializer(plane)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )
    if request.method == 'PUT':
        serializer = PlaneSerialializer(plane, data=request.data)
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
        plane.delete()
        return Response(
            'Delete successfully',
            status=status.HTTP_202_ACCEPTED

        )