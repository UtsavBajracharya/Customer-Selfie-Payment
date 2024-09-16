from django.db import models
from django.contrib.auth.models import User

class AppUser(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	phone = models.IntegerField()
	funds = models.IntegerField(blank=True,null=True,default=0)
	


 