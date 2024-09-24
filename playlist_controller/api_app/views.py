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

from django.http import JsonResponse

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
    # directory and link this view to a url.

# When we call the GetRoom view with a GET request, we need to pass a parameter
# in the url named code.  That code will be the room we are trying to get.
class GetRoom(APIView):
    serializer_class = RoomSerializer
    lookup_url_kawrg = 'code'
    
    def get(self, request, format=None):
        # request.GET will return a dictionary of all the parameters passed in
        # the URL string of a GET request.
        # .get(self.lookup_url_kawrg) will retrieve from that dictionary the
        # value of the self.lookup_url_kawg parameter.  It will then be stored
        # as the code.
        code = request.GET.get(self.lookup_url_kawrg)
        # If code contains a value...
        if code != None:
            # Filter all the rooms for the one where the room's code = the code.
            # Store that room in room.  Room is a list.
            room = Room.objects.filter(code=code)
            # If there was a room stored, its length will be greater than 0.
            if len(room) > 0:
                # Serialize the room and extract its data (a dictionary).
                data = RoomSerializer(room[0]).data
                # Add a new key, "is_host", to the room's dictionary.
                # See if the user who sent the GET request is the host of the room
                # whose code matches.  If yes, the value is True, else, False.
                data["is_host"] = self.request.session.session_key == room[0].host

                return Response(data, status=status.HTTP_200_OK)
            
            return Response({'Room Not Found': 'Invalid Room Code.'}, status=status.HTTP_404_NOT_FOUND)

        return Response({'Bad Request': 'Code parameter not found in request'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Note: After defining the view, we need to go to urls.py inside the api_app
        # directory and link this view to a url.

class JoinRoom(APIView):
    lookup_url_kawrg = 'code'
    
    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            # Create a new session.
            self.request.session.create()
            
        code = request.data.get(self.lookup_url_kawrg)
        if code != None:
            room_result = Room.objects.filter(code=code)
            if len(room_result) > 0:
                room = room_result[0]
                self.request.session["room_code"] = code
                return Response({"message": "Room Joined!"}, status=status.HTTP_200_OK)
            
            return Response({"Bad Request": "Invalid Room Code"}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response({"Bad Request": "Invalid post data, did not find a room"}, status=status.HTTP_400_BAD_REQUEST)

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
                guest_can_pause = serializer.data.get('guest_can_pause')
                votes_to_skip = serializer.data.get('votes_to_skip')
                host = self.request.session.session_key
                # Look for any rooms in the database that have the same host as
                # the host who is currently trying to create a new room.
                queryset = Room.objects.filter(host=host)
                # If one exists...
                if queryset.exists():
                    # Set room to the first element in the queryset.
                    room = queryset[0]
                    # Set the room's fields to the values from the serializer.
                    room.guest_can_pause = guest_can_pause
                    room.votes_to_skip = votes_to_skip
                    # Save the room to update it, passing it the fields we want
                    # to update.
                    room.save(update_fields=['guest_can_pause', 'votes_to_skip'])
                    
                    self.request.session['room_code'] = room.code
                    # Return a response containing a serialized version of the 
                    # room and a status code OK.
                    return Response(RoomSerializer(room).data, status=status.HTTP_200_OK)
                # Otherwise one doesn't exist...
                else:
                    # Create a new room, setting its fields to the values above.
                    room = Room(host=host, guest_can_pause=guest_can_pause, votes_to_skip=votes_to_skip)
                    # Save the room (without fields because we're not updating.)
                    room.save()
                    
                    self.request.session['room_code'] = room.code
                    # Return a response containing a serialized version of the
                    # room and a status code for CREATED.
                    return Response(RoomSerializer(room).data, status=status.HTTP_201_CREATED)
            # Otherwise, serializer is not valid...
            else:
                # Return a response detailing error and status code BAD REQUEST.
                return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)

class UserInRoom(APIView):
    def get(self, request, format=None):
        # Checking if a user has a current session.  If it doesn't...
        if not self.request.session.exists(self.request.session.session_key):
            # Create a new session.
            self.request.session.create()
            
        data = {
            "code": self.request.session.get("room_code")
        }
        
        return JsonResponse(data, status=status.HTTP_200_OK)