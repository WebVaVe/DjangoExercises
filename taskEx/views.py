from asyncio import tasks
from audioop import reverse
from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse


import taskEx

# Create your views here.
def index (request):
    if "task" not in request.session:
        request.session['task'] = []
    return render(request, "taskEx/task.html", {
        "task" : request.session['task']
    })
class NewTask(forms.Form):
    tasks = forms.CharField(label = "your Task")
    age = forms.IntegerField(label = "PUT YOR age",min_value= 1,max_value= 16)

def add (request):
    if request.method == "POST":
        form = NewTask(request.POST)
        if form.is_valid():
            addTask = form.cleaned_data['tasks']
            request.session['task'] += [addTask]
            return HttpResponseRedirect(reverse("taskEx:index"))
        else:
            return render (request,"taskEx/add.html",{
                 "addForm" : form
        })
#clean data for delete time and ... data
    return render (request, "taskEx/add.html",{
        "form" : NewTask()
    })