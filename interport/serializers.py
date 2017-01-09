from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Person 


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person 
        fields = ('city','country','age')

