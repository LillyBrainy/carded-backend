from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User , on_delete = models.CASCADE)
	bio = models.TextField(null = True , blank = True)
	link = models. URLField(null = True , blank = True)

	def __str__(self):
		return self.user

class UserInfo(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	name = models.CharField(max_length = 200)
	company_name = models.CharField(max_length = 300 , null = True, blank = True)
	email = models.EmailField( null = True, blank = True)
	phone_number1 = models.CharField(max_length = 100,  null = True, blank = True)
	phone_number2 = models.CharField(max_length = 100,  null = True, blank = True)
	social_media = models.URLField( null = True, blank = True)

	def __str__(self):
		return self.user.username


# class Contacts(models.Model):
# 	user = models.ForeignKey(User, on_delete = models.CASCADE)
# 	userinfo = models.ForeignKey(UserInfo, on_delete = models.CASCADE)
# 	# company_name = models.CharField(max_length = 300 , null = True, blank = True)
# 	# email = models.EmailField( null = True, blank = True)
# 	# phone_number1 = models.CharField(max_length = 100,  null = True, blank = True)
# 	# phone_number2 = models.CharField(max_length = 100,  null = True, blank = True)
# 	# social_media = models.URLField( null = True, blank = True)

# 	def __str__(self):
# 		return self.user.username




class Follow(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	friends = models.ForeignKey(User, on_delete = models.CASCADE , related_name = 'following')			
	
	def __str__(self):
		return self.user.username