from django.db import models
from restaurant.models import RestaurantModel


class MenuModel(models.Model):
    name = models.CharField(max_length=100)
    date_field = models.DateField(auto_now_add=True)
    like = models.IntegerField(default=0)
    restaurant_foren = models.ForeignKey(RestaurantModel, on_delete=models.CASCADE)


class ProductModel(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    menu_foren = models.ForeignKey(MenuModel, on_delete=models.CASCADE)
