# This is a Django-created file.
# This is where the url will be sent initially.  From here, the url will
# be forwarded to the correct location. 


from django.contrib import admin
from django.urls import path
# Import allowing us to called the include function in the path below.
from django.urls import include


urlpatterns = [
    # '' means all endpoints,
    # will be forwarded to the user-created urls.py file in the api_app folder.
    path('', include('api_app.urls')),
]
