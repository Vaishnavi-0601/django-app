from django.urls import path
from . import views

urlpatterns=[

path('list', views.car_list_view),
path('<int:pk>',views.car_details,name='car_detail'),
path('showroom',views.Showroom_view.as_view()),
path('showroom/<int:pk>',views.Showroom_particular.as_view())


]