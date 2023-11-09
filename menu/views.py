from .models import MenuModel, ProductModel

from .serializer import GetMenuModelSerializer, ProductModelSerializer, MenuModelSerializer

from rest_framework.permissions import AllowAny
from rest_framework import generics
from rest_framework.response import Response

from adminsite.pagination import CustomPagination
from datetime import date

from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.core.cache import cache

class GetMenuView(generics.ListAPIView):

    today = date.today()
    # Фильтрация по текущему дню

    queryset = MenuModel.objects.filter(
        date_field__year=today.year,
        date_field__month=today.month,
        date_field__day=today.day
    ).order_by('-like')


    serializer_class = GetMenuModelSerializer


class GetMenuMostLikeView(generics.GenericAPIView):
    cache.clear()


    serializer_class = GetMenuModelSerializer

    def get(self, request, *args, **kwargs):
        today = date.today()
        queryset = MenuModel.objects.filter(
            date_field__year=today.year,
            date_field__month=today.month,
            date_field__day=today.day
        ).order_by('-like').first()
        serializer = self.get_serializer(queryset)
        return Response(serializer.data)


class RUDMenuView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuModel.objects.all()
    serializer_class = MenuModelSerializer


class RMenuView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuModel.objects.all()
    serializer_class = GetMenuModelSerializer


class CreateMenuView(generics.CreateAPIView):
    queryset = MenuModel.objects.all()
    serializer_class = MenuModelSerializer


class RUDProductView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductModelSerializer


class CreateProductView(generics.CreateAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductModelSerializer


