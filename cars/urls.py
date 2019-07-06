from django.urls import path
from . import views

urlpatterns = [
    path('', views.car_view, name='cars'),
    #path('', views.ListCarsView.as_view(), name='cars'), #этап 1
]