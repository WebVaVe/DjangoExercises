from django.urls import path,include
import datetime
from . import views

urlpatterns = [
    path ("", views.index,name = "taskEx"),
    path ("add", views.add, name = "add")
]
