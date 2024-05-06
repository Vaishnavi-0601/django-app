from django.urls import path
from . import views

urlpatterns=[

path('list', views.car_list_view),
path('<int:pk>',views.car_details),


]