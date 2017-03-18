from __future__ import unicode_literals

from django.db import models

# Create your models here.

class otp_info(models.Model):
	mobile= models.IntegerField(primary_key=True, null=False)
	otp= models.PositiveSmallIntegerField(default=0,null=True)
	flag=models.BooleanField(default=False)
	modified= models.DateTimeField(auto_now=True,auto_now_add=False)
	created= models.DateTimeField(auto_now=False,auto_now_add=True)
	access_token=models.CharField(max_length=500,blank=True,null=True) 
