from django.shortcuts import render
from Dog_App.models import Dog
from Dog_App.serializers import DogSerializer
from rest_framework import generics
# Create your views here.
class DogViewSet(generics.ListCreateAPIView):
    """
    retrieve: Return the given dog.

    list: Return a list of all dogs.

    create:
        Create a new dog.

    destroy:
        Delete a dog.

    update:
        Update a dog.

    partial_update:
        Update a dog.
    """

    queryset = Dog.objects.all()
    serializer_class = DogSerializer


