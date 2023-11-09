from django.urls import path
from .views import * # RUDRestaurantView CreateRestaurantView,

urlpatterns = [
    path('get/', GetMenuView.as_view()),
    path('most_like/', GetMenuMostLikeView.as_view()),
    path('create/', CreateMenuView.as_view()),
    path('rud/<int:pk>/', RUDMenuView.as_view()),
    path('get/<int:pk>/', RMenuView.as_view()),
    path('product/create/', CreateProductView.as_view()),
    path('product/rud/<int:pk>/', RUDProductView.as_view()),
]
