from django.shortcuts import render

# Create your views here.
task = ["homework", "lern english", "programin"]
def index (request):
    return render(request, "taskEx/task.html", {
        "task" : task
    })
def add (request):
    return render (request, "taskEx/add.html")