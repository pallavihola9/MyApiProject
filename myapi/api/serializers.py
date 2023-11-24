from .models import *
from rest_framework import serializers

class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisterUser
        fields = '__all__'