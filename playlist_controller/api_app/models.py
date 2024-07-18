from django.db import models
# Imports to be used in the helper function below.
import string
import random

# Helper function to generate a unique room code to assign to a newly created
# room.
def generate_unique_code():
    length = 6 # The length we want the code to be.
    
    # Until we generate a code that is unique...
    while True:
        # ...join a random selection of uppercase letters equaling length 6.
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        # To determine if this code is in fact unique, check each of the rooms
        # to see if they have this code already.  
        # Room.objects is all of the rooms,
        # .filter(code=code) grabs only the ones where their code equals the
        # code we just created,
        # .count() then counts the number of the rooms that were just 
        # "filtered in" (meaning meets the criteria code=code).
        # If the count is 0, then the code we just created is indeed unique.
        if Room.objects.filter(code=code).count() == 0:
            break
    
    return code
        

# Create your models here.  
# Instead of creating tables, we define models.

class Room(models.Model):
    # Each room will have a code...
    # ...that is sequence of chars, with a max length of 8, and is unique.
    code = models.CharField(max_length=8, default=generate_unique_code, unique=True)
    # Each room will have a host...
    # ...that is sequence of chars, with a max length of 50, and is unique.
    host = models.CharField(max_length=50, unique=True)
    # Permission that determines whether a guest is allowed to pause the music
    # (either True or False.)  It will not be left empty, is False by default.
    guest_can_pause = models.BooleanField(null=False, default=False)
    # Each room will have a count of the number of votes to skip...
    votes_to_skip = models.IntegerField(null=False, default=1)
    # auto_now_add means the date and time will automatically be added to the
    # Room model when it is created.
    created_at = models.DateTimeField(auto_now_add=True)