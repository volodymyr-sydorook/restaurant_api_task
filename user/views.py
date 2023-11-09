from rest_framework import generics
from .serializer import UserSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
