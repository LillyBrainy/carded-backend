from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class Profile(models.Model):
# 	user = models.OneToOneField(User , on_delete = models.CASCADE)
# 	bio = models.TextField(null = True , blank = True)
# 	link = models. URLField(null = True , blank = True)

# 	def __str__(self):
# 		return self.user

class PhoneNumber(models.Model):
	number = models.CharField(max_length = 100)

class Profile(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'user_info') #changed from onetoone to foreignkey for multiple bar codes 
	profile_name = models.CharField(max_length = 200)
	first_name = models.CharField(max_length = 200, null = True, blank = True)
	last_name = models.CharField(max_length = 200, null = True, blank = True)
	company_name = models.CharField(max_length = 300 , null = True, blank = True)
	email = models.EmailField( null = True, blank = True)
	phone_number = models.ManyToManyField(PhoneNumber)
	# phone_number2 = models.CharField(max_length = 100,  null = True, blank = True) !! create a phone# model and let phone number field be a relationship to it (manytomany)
	social_media = models.URLField( null = True, blank = True) # make social media field into charfields so users can add their handles and make it manytomany to socialmedia model

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
	profile = models.ForeignKey(Profile, on_delete = models.CASCADE , related_name = 'followers')			
	
	def __str__(self):
		return self.user.username