"""carded URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_jwt.views import obtain_jwt_token
from coded.views import UserRegistrationAPIView , UserFillInfoAPIView ,UserDataAPIView , UserRetraiveInfoAPIView,FollowUserAPIView, MyContactListAPIView, FillUserInfoAPIView 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', obtain_jwt_token),
    path('signup/', UserRegistrationAPIView.as_view(), name = 'signup'),
    path('fill/QRInfo/<int:userinfo_id>/', UserFillInfoAPIView.as_view(), name = 'fill-QR'),
    path('get/userInfo/<int:userinfo_id>/', UserRetraiveInfoAPIView.as_view(), name = 'get-info'),
    path('user/<int:user_id>/data/', UserDataAPIView.as_view(), name = 'user-data'),
    path('follow/<int:user_id>/user/', FollowUserAPIView.as_view(), name = 'follow-user'),
    path('contacts/', MyContactListAPIView.as_view(), name = 'contacts'),
    path('fill/<int:userinfo_id>/info/',FillUserInfoAPIView.as_view(), name = 'fill-info' ),
]

urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)