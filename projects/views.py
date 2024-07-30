from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Project
from .forms import ProjectForm

# Create your views here.
def projects(request):
    msg = "Projects your fellow developers made"
    projectsList = Project.objects.all()
    return render(request, 'projects/projects.html', context={'message':msg, 'projects': projectsList})

def project(request, pk):
    projectObj = Project.objects.get(id = pk)
    tags = projectObj.tags.all()
    return render(request, 'projects/single-project.html', context = {'project':projectObj, 'tags': tags})

def createProject(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')
    return render(request, 'projects/project_form.html', context = {'form': form})

def updateProject(request, pk):
    item = Project.objects.get(id=pk)
    form = ProjectForm(instance=item)
    if request.method == 'POST':
        form = ProjectForm(request.POST,request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('projects')
    return render(request, 'projects/project_form.html', context = {'form': form})

def deleteProject(request, pk):
    item = Project.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('projects')
    return render(request, 'projects/delete_object.html', context= {'project': item})
