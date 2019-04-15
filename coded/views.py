from django.shortcuts import render
from .serializers import UserRegistrationSerializer 
from rest_framework.generics import CreateAPIView , RetrieveUpdateAPIView , DestroyAPIView, ListAPIView ,RetrieveAPIView
# from .models import Card

# Create your views here.

class UserRegistrationAPIView(CreateAPIView):
	serializer_class = UserRegistrationSerializer

# class CreateCardAPIView(CreateAPIView):
# 	serializer_class = CardSerializer

# 	def perform_create(self,serializer):
# 		serializer.save(author = self.request.user)

		

