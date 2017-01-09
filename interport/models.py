from django.db import models
from django.contrib.auth.models import User


"""
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	description = models.TextField(null=True, blank=True)
	country = models.CharField(max_length=30, blank=True)
	age = models.CharField(max_length=30, blank=True)
"""

"""
class CarouselItem(models.Model):
	image: models.ImageField(upload_to = 'static/pictures')
	url: models.CharField(max_length=30, default=None , blank=True)
	person: models.CharField(max_length=30, blank=True)
	country: models.CharField(max_length=30, blank=True)
"""



