from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request,name):
    return HttpResponse(f"<h1>Hello {name.capitalize()}</h1>")
#capitalize for captal one character on name captal
def index (request):
    return render(request, "oneEx/index.html")
