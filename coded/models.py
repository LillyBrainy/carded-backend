from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User , on_delete = models.CASCADE)
	bio = models.TextField(null = True , blank = True)
	link = models. URLField(null = True , blank = True)

	def __str__(self):
		return self.user

# class Contact(models.Model):
# 	user = models.ForeignKey(User, on_delete = models.CASCADE)
# 	name = models.CharField(max_length = 200)
# 	company_name = models.CharField(max_length = 300)
# 	description = models.TextField(max_length = 400)
# 	email = models.EmailField()
# 	phone_number1 = models.CharField(max_length = 100)
# 	phone_number2 = models.CharField(max_length = 100)
# 	location = models.URLField()		