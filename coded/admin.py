from django.contrib import admin
from .models import Profile,UserInfo , Follow

# Register your models here.
admin.site.register(Profile)
admin.site.register(UserInfo)
admin.site.register(Follow)