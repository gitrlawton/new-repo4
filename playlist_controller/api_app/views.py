# Django-created file.

from django.shortcuts import render

# Allows us to create a class that inherits from a generic API view.
from rest_framework import generics
# Import the RoomSerializer and the Room model.
from .serializers import RoomSerializer, CreateRoomSerializer
from .models import Room
# 
from rest_framework.views import APIView
# So we can send a custom response from our view.
from rest_framework.response import Response
# Gives us access to http status codes which we'll use with our response.
from rest_framework import status

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

class CreateRoomView(APIView):
    serializer_class = CreateRoomSerializer
    
    def post(self, request, format=None):
        # Checking if a user has a current session.  If it doesn't...
        if not self.request.session.exists(self.request.session.session_key):
            # Create a new session.
            self.request.session.create()
        else:
            # Take our data and serialize it.
            serializer = self.serializer_class(data=request.data)
            # Determine if the fields we defined are valid and present in the 
            # data we serialized.  If the serailized data is valid...
            if serializer.is_valid():
                # Extract the data back into its fields.  Note: these are the
                # pieces of information need to create a new room.
                guest_can_pause = serializer.data.guest_can_pause
                votes_to_skip = serializer.data.votes_to_skip
                host = self.request.session.session_key
                