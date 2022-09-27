from django.shortcuts import render
from . import urls

# Create your views here.
def index(request,name):
    return render(request, "twoEx/name.html",{
        "name" : name.capitalize(),
    })