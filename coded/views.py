from django.shortcuts import render
from .serializers import UserRegistrationSerializer , UserInfoSerializer , UserDataSerializer, FollowSerializer, PhoneNumberSerializer
from rest_framework.generics import CreateAPIView , RetrieveUpdateAPIView , DestroyAPIView, ListAPIView ,RetrieveAPIView 
from rest_framework.views import APIView
from .models import  Follow
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
# from .models import Card

# Create your views here.

class UserRegistrationAPIView(CreateAPIView):
    serializer_class = UserRegistrationSerializer

# class CreateCardAPIView(CreateAPIView):
#   serializer_class = CardSerializer

#   def perform_create(self,serializer):
#       serializer.save(author = self.request.user)

# class UserFillInfoAPIView(RetrieveUpdateAPIView):
#   queryset = UserInfo.objects.all()
#   serializer_class =  UserInfoSerializer
#   lookup_fields = 'id'
#   lookup_url_kwarg = 'userinfo_id'

class UserUpdateInfoAPIView(APIView):
    def get(self,request):
        user = request.user
        userinfo = user.user_info.all()
        return Response(UserInfoSerializer(userinfo, many = True).data)

    def put(self, request):
        userinfo = request.user.user_info.get(id=request.data.get("id"))
        serializer = UserInfoSerializer(userinfo, data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        serializer = UserInfoSerializer(data=request.data)
        if serializer.is_valid():

            serializer.save(user=request.user)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    
# create api view ()
###
"""
1. define a APIView from DjangoRestFramework
2. Create a 'get' method inside that view
3. the method will retrieve the current logged in user  // request.user
4. return the userinfo object relating to that user

1. create a 'post' method inside the same view
2. look at the user registration method for more clues on how to update and return a message 
"""
###



# class UserRetrieveInfoAPIView(RetrieveAPIView):
#   queryset = UserInfo.objects.all()
#   serializer_class =  UserInfoSerializer
#   lookup_fields = 'id'
#   lookup_url_kwarg = 'userinfo_id'        

class UserDataAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class =  UserDataSerializer
    lookup_fields = 'id'
    lookup_url_kwarg = 'user_id'


class FollowUserAPIView(APIView):
    def post(self, request, user_id):
            user = User.objects.get(id = user_id)
            noteG = request.data.get('note')
            follow_obj, created = Follow.objects.get_or_create(user = request.user , friends = user , note = noteG )
            # if created:
            #     action = 'follow'
            # else:
            #     action = 'unfollow'
            #      # follow_obj.delete()
            # return Response({"follow": action})
            return Response()   


class MyContactListAPIView(ListAPIView):
    def get_queryset(self):
        return Follow.objects.filter(user=self.request.user)

    serializer_class = FollowSerializer
    



