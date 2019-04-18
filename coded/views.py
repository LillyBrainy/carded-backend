from django.shortcuts import render
from .serializers import UserRegistrationSerializer , UserInfoSerializer , UserDataSerializer
from rest_framework.generics import CreateAPIView , RetrieveUpdateAPIView , DestroyAPIView, ListAPIView ,RetrieveAPIView 
from rest_framework.views import APIView
from .models import UserInfo , Follow
from django.contrib.auth.models import User
from rest_framework.response import Response
# from .models import Card

# Create your views here.

class UserRegistrationAPIView(CreateAPIView):
	serializer_class = UserRegistrationSerializer

# class CreateCardAPIView(CreateAPIView):
#   serializer_class = CardSerializer

#   def perform_create(self,serializer):
#       serializer.save(author = self.request.user)

class UserFillInfoAPIView(RetrieveUpdateAPIView):
	queryset = UserInfo.objects.all()
	serializer_class =  UserInfoSerializer
	lookup_fields = 'id'
	lookup_url_kwarg = 'userinfo_id'
	

class UserRetraiveInfoAPIView(RetrieveAPIView):
	queryset = UserInfo.objects.all()
	serializer_class =  UserInfoSerializer
	lookup_fields = 'id'
	lookup_url_kwarg = 'userinfo_id'        

class UserDataAPIView(RetrieveAPIView):
	queryset = User.objects.all()
	serializer_class =  UserDataSerializer
	lookup_fields = 'id'
	lookup_url_kwarg = 'user_id'


class FollowUserAPIView(APIView):
	def post(self, request, user_id):
			user = User.objects.get(id = user_id)
			follow_obj, created = Follow.objects.get_or_create(user = request.user , friends = user)
			# if created:
			#     action = 'follow'
			# else:
			#     action = 'unfollow'
			#      # follow_obj.delete()
			# return Response({"follow": action})
			return Response()   
