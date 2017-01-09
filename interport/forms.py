from django import forms
from django.contrib.auth.models import User
#from .models import Profile

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = User		
		fields = ('first_name', 'last_name', 'email', 'username',)



""""
class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('country','age','description',)
"""

"""
class CarouselItemForm(forms.ModelForm):
	model = CarouselItem
	image: forms.ImageField()
	url: forms.CharField(max_length=30)
	person: forms.CharField(max_length=30)
	country: forms.CharField(max_length=30)
"""





