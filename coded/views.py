from django.shortcuts import render
from .serializers import UserRegistrationSerializer
from rest_framework.generics import CreateAPIView

# Create your views here.

class UserRegistrationAPIView(CreateAPIView):
	serializer_class = UserRegistrationSerializer
