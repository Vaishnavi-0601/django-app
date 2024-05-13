from django.shortcuts import render
from .models import Carlist,Showroomlist,Review
from django.http import JsonResponse
from django.http import HttpResponse
from .api_files.serializers import CarSerializer,ShowroomSerializer,ReviewSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
# Create your views here.


# def car_list_view(request):
#     cars=Carlist.objects.all()
#     data={
#         'cars': list(cars.values()),
    
#     }
#     # json_data=json.dumps(data)
#     return JsonResponse(data)
#     # return HttpResponse(json_data, content_type='application/json')

# def car_details(request,pk):
#     car=Carlist.objects.get(pk=pk)
#     data={
#         'name': car.name,
#         'description': car.description,
#         'active status': car.active
#     }
#     return JsonResponse(data)

@api_view(['GET','POST'])
def car_list_view(request):
    if request.method=='GET':

        car=Carlist.objects.all()
        serializer=CarSerializer(car, many=True)
        return Response(serializer.data)
    if request.method=='POST':
        serializer=CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def car_details(request,pk):
    if request.method=='GET':
        try:
            car=Carlist.objects.get(pk=pk)
        except:
            return Response('Error:Car not found')
        serializer=CarSerializer(car)
        return Response(serializer.data)
    if request.method=='PUT':
        car=Carlist.objects.get(pk=pk)
        serializer=CarSerializer(car,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    if request.method=='DELETE':
        car=Carlist.objects.get(pk=pk)
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class Showroom_view(APIView):
    def get(self,request):
        showroom=Showroomlist.objects.all()
        serializer=ShowroomSerializer(showroom,many=True,context={'request': request})
        return Response(serializer.data)

    def post(self,request):
        serializer=ShowroomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
            
class Showroom_particular(APIView):

    def get(self,request,pk):
        try:
            showroom=Showroomlist.objects.get(pk=pk)
            serializer=ShowroomSerializer(showroom)
            return Response(serializer.data)
        except:
            return Response('error:no showroom',status=status.HTTP_400_BAD_REQUEST) 

    def put(self,request,pk):
        showroom=Showroomlist.objects.get(pk=pk)
        serializer=ShowroomSerializer(showroom,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_204_NO_CONTENT)
    
    def delete(self,request,pk):
        showroom=Showroomlist.objects.get(pk=pk)
        showroom.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Review_view(APIView):
    def get(self,request):
        review=Review.objects.all()
        serializer=ReviewSerializer(review,many=True)
       
        return Response(serializer.data)
        

    def post(self,request):
        serializer=ReviewSerializer(review,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
