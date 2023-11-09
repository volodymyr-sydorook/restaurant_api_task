from rest_framework import serializers
from .models import RestaurantModel


class RestaurantModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantModel
        fields = ('id', 'name', 'location')
