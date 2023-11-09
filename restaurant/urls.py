from django.urls import path
from .views import CreateRestaurantView, GetRestaurantView, RUDRestaurantView

urlpatterns = [
    path('get/', GetRestaurantView.as_view()),
    path('create/', CreateRestaurantView.as_view()),
    path('rud/<int:pk>/', RUDRestaurantView.as_view()),
]
