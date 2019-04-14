from rest_framework import serializers
from .models import Profile
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only = True)
	token = serializers.CharField(read_only = True , allow_blank = True)
	class Meta:
		model = User
		fields = ['username', 'password', 'token','first_name', 'last_name']

	def create(self, validated_data):
		username = validated_data['username']
		password = validated_data['password']
		new_user = User(username = username)
		new_user.set_password(password)
		new_user.save()
		Profile.objects.create(user = new_user)
		jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
		jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
		payload = jwt_payload_handler(new_user)
		token = jwt_encode_handler(payload)
		validated_data['token'] = token
		return validated_data




    

