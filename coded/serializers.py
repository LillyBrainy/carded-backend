from rest_framework import serializers
from .models import Profile , Follow
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
        # Profile.objects.create(user = new_user)
        # UserInfo.objects.create(user = new_user)
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(new_user)
        token = jwt_encode_handler(payload)
        validated_data['token'] = token
        return validated_data

# class PhoneNumberSerializer(serializers.ModelSerializer):
#     id = serializers.CharField(required=False)
#     class Meta:
#         model = PhoneNumber
#         fields = ['number', 'id']

class ProfileSerializer(serializers.ModelSerializer):
    # phone_number = PhoneNumberSerializer(many=True)
    class Meta:
        model = Profile
        fields = '__all__'
        read_only_fields = ['user']

    # def create(self, validated_data):
    #     phonenumbers_data = validated_data.pop('phone_number')
    #     profile = Profile.objects.create(**validated_data)
    #     for phonenumber_data in phonenumbers_data:
    #         phone_number, created = PhoneNumber.objects.get_or_create(number=phonenumber_data.get("number", ""))
    #         profile.phone_number.add(phone_number)

    #     return profile

    # def update(self, instance, validated_data):
    #     phonenumbers_data = validated_data.pop('phone_number')
    #     profile = instance

    #     profile.profile_name = validated_data.get("profile_name", profile.profile_name)
    #     profile.first_name = validated_data.get("first_name", profile.first_name)
    #     profile.last_name = validated_data.get("last_name", profile.last_name)
    #     profile.company_name = validated_data.get("company_name", profile.company_name)
    #     profile.email = validated_data.get("email", profile.email)
    #     profile.save()

    #     for phonenumber_data in phonenumbers_data:
    #         phonenumber_id = phonenumber_data.get('id', "NAN")
    #         if phonenumber_id != "NAN":
    #             phone_number = profile.phone_number.get(id=int(phonenumber_id))
    #             phone_number.number = phonenumber_data.get("number", phone_number.number)
    #             phone_number.save()
    #         else:
    #             phone_number, created = PhoneNumber.objects.get_or_create(number=phonenumber_data.get("number", ""))
    #             profile.phone_number.add(phone_number)

    #     return profile


class UserDataSerializer(serializers.ModelSerializer):
    profiles = ProfileSerializer(many=True)
    class Meta:
        model = User
        fields = ['id','username','profiles']

class FollowSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    class Meta:
        model = Follow
        fields = ['note' ,'profile']


                        




    

