from rest_framework import serializers
from .models import Profile , UserInfo, Follow, PhoneNumber
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
        # UserInfo.objects.create(user = new_user)
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(new_user)
        token = jwt_encode_handler(payload)
        validated_data['token'] = token
        return validated_data

class PhoneNumberSerializer(serializers.ModelSerializer):
    id = serializers.CharField(required=False)
    class Meta:
        model = PhoneNumber
        fields = ['number', 'id']

class UserInfoSerializer(serializers.ModelSerializer):
    phone_number = PhoneNumberSerializer(many=True)
    class Meta:
        model = UserInfo
        fields = '__all__'
        read_only_fields = ['user']

    def create(self, validated_data):
        phonenumbers_data = validated_data.pop('phone_number')
        userinfo = UserInfo.objects.create(**validated_data)
        for phonenumber_data in phonenumbers_data:
            phone_number, created = PhoneNumber.objects.get_or_create(number=phonenumber_data.get("number", ""))
            userinfo.phone_number.add(phone_number)

        return userinfo

    def update(self, instance, validated_data):
        phonenumbers_data = validated_data.pop('phone_number')
        userinfo = instance

        userinfo.profile_name = validated_data.get("profile_name", userinfo.profile_name)
        userinfo.first_name = validated_data.get("first_name", userinfo.first_name)
        userinfo.last_name = validated_data.get("last_name", userinfo.last_name)
        userinfo.company_name = validated_data.get("company_name", userinfo.company_name)
        userinfo.email = validated_data.get("email", userinfo.email)
        userinfo.save()

        for phonenumber_data in phonenumbers_data:
            phonenumber_id = phonenumber_data.get('id', "NAN")
            if phonenumber_id != "NAN":
                phone_number = userinfo.phone_number.get(id=int(phonenumber_id))
                phone_number.number = phonenumber_data.get("number", phone_number.number)
                phone_number.save()
            else:
                phone_number, created = PhoneNumber.objects.get_or_create(number=phonenumber_data.get("number", ""))
                userinfo.phone_number.add(phone_number)

        return userinfo


class UserDataSerializer(serializers.ModelSerializer):
    user_info = UserInfoSerializer(many=True)
    class Meta:
        model = User
        fields = ['id','username','user_info']

class FollowSerializer(serializers.ModelSerializer):
    friends = UserDataSerializer()
    class Meta:
        model = Follow
        fields = ['friends']


                        




    

