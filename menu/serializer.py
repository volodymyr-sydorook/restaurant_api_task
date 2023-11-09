from rest_framework import serializers
from .models import MenuModel, ProductModel
from restaurant.models import RestaurantModel
from restaurant.serializer import RestaurantModelSerializer


class ProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = ('__all__')


class MenuModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuModel
        fields = ('__all__')


class GetMenuModelSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()
    product = serializers.SerializerMethodField()
    restaurant_foren = RestaurantModelSerializer()  # Изменение здесь

    class Meta:
        model = MenuModel
        fields = ['id', 'name', 'like', 'total_price', 'restaurant_foren', 'date_field', 'product']

    def get_total_price(self, obj):
        all_product = ProductModel.objects.filter(menu_foren=obj)
        total_price = 0
        for el in all_product:
            total_price += el.price
        return total_price

    def get_product(self, obj):
        all_product = ProductModel.objects.filter(menu_foren=obj)
        serializer = ProductModelSerializer(all_product, many=True)
        return serializer.data
