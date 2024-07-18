# User-created file.
# Serializes will take our model, which has a bunch of python code, and 
# translate it into a json.

from rest_framework import serializers
# Import the model(s) so we can serialize them.
from .models import Room

# Serializes a Room.
class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        # The model we want to serialize.
        model = Room
        # The model's fields we want to serialize.
        # We want to include the 'id' field, even though it isn't defined in
        # the models.py file.  This will be its primary key.
        fields = ('id', 'code', 'host', 'guest_can_pause', 'votes_to_skip', 'created_at')
        
# Serializes a request (POST request because we'll be creating something new.)
class CreateRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        # Just the fields we want to be serialized.
        fields = ('guest_can_pause', 'votes_to_skip')