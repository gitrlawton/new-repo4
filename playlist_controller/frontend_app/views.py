from django.shortcuts import render

# Create your views here.

def index(request, *args, **kwargs):
    # Render the index.html template.
    return render(request, "frontend/index.html")