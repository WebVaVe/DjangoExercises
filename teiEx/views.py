from calendar import month
from http.client import HTTPResponse
from django.shortcuts import render
import datetime

# Create your views here.
def index (request):
    day = datetime.datetime.now()
    return render (request,"teiEx/day.html",{
        "now" : day,
         "newyear" : day.month == 1 and day.day == 1
 })
