# from django import serializers
from Dog_App.models import Dog
from rest_framework import serializers

class DogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields = ['name' , 'color']