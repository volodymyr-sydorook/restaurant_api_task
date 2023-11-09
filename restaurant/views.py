from .models import RestaurantModel

from .serializer import RestaurantModelSerializer

from rest_framework.permissions import AllowAny
from rest_framework import generics

from adminsite.pagination import CustomPagination


class GetRestaurantView(generics.ListAPIView):
    queryset = RestaurantModel.objects.all()
    serializer_class = RestaurantModelSerializer


class RUDRestaurantView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RestaurantModel.objects.all()
    serializer_class = RestaurantModelSerializer


class CreateRestaurantView(generics.CreateAPIView):
    queryset = RestaurantModel.objects.all()
    serializer_class = RestaurantModelSerializer
