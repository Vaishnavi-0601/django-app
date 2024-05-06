from django.shortcuts import render
from .models import Carlist
from django.http import JsonResponse
from django.http import HttpResponse
from .api_files.serializers import CarSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
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

@api_view()
def car_list_view(request):
    car=Carlist.objects.all()
    serializer=CarSerializer(car, many=True)
    return Response(serializer.data)

@api_view()
def car_details(request,pk):
    car=Carlist.objects.get(pk=pk)
    serializer=CarSerializer(car)
    return Response(serializer.data)
