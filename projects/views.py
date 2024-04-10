from django.http import HttpResponse
from django.shortcuts import render
from .models import Project
from .forms import ProjectForm

# Create your views here.
def projects(request):
    msg = "Below are the list of all the projects"
    projectsList = Project.objects.all()
    return render(request, 'projects/projects.html', context={'message':msg, 'projects': projectsList})

def project(request, pk):
    projectObj = Project.objects.get(id = pk)
    tags = projectObj.tags.all()
    return render(request, 'projects/single-project.html', context = {'project':projectObj, 'tags': tags})

def createProject(request):
    form = ProjectForm()
    context= {'form' : form}
    return render(request, 'projects/project_form.html', context)