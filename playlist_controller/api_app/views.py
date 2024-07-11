# Django-created file.

from django.shortcuts import render

# Allows us to create a class that inherits from a generic API view.
from rest_framework import generics
# Import the RoomSerializer and the Room model.
from .serializers import RoomSerializer
from .models import Room

# Create your views here.

# This is an API View.  It inherits from a generic API view.
# Below, we set it up to gather all the rooms that exist and return it as json.
# ListAPIView will just show the json data when it is visited.  It is used for
# receiving GET requests.  CreateAPIView would show an input form when visited.
# That would be used for receiving POST requests.
class RoomView(generics.ListAPIView):
    # Gather all the rooms.
    querySet = Room.objects.all()
    serializer_class = RoomSerializer
    
# Note: After defining the view, we need to go to urls.py inside the api_app
# directory and link this view toa url.