from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Project
from .forms import ProjectForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def projects(request):
    msg = "Projects your fellow developers made"
    projectsList = Project.objects.all()
    return render(request, 'projects/projects.html', context={'message':msg, 'projects': projectsList})

def project(request, pk):
    projectObj = Project.objects.get(id = pk)
    tags = projectObj.tags.all()
    return render(request, 'projects/single-project.html', context = {'project':projectObj, 'tags': tags})

@login_required(login_url='login')
def createProject(request):
    profile = request.user.profile
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit = False) # return instance of current project
            project.owner = profile
            project.save()
            return redirect('projects')
    return render(request, 'projects/project_form.html', context = {'form': form})

@login_required(login_url='login')
def updateProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method == 'POST':
        form = ProjectForm(request.POST,request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
    return render(request, 'projects/project_form.html', context = {'form': form})

@login_required(login_url='login')
def deleteProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    return render(request, 'projects/delete_object.html', context= {'project': project})
