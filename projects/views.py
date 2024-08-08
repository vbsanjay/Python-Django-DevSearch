from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from .models import Project, Tag
from .forms import ProjectForm
from .utils import searchProjects

# Create your views here.
def projects(request):
    projectsList, search_query = searchProjects(request)

    page = request.GET.get('page')
    results = 3
    paginator = Paginator(projectsList, results)

    try:
        projectsList = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        projectsList = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        projectsList = paginator.page(page)

    leftIndex = (int(page) - 4)

    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 5)

    if rightIndex  > paginator.num_pages:
        rightIndex = paginator.num_pages + 1
    
    custom_range = range(leftIndex, rightIndex)

    context = {'projects': projectsList, 'search_query': search_query, 
               'paginator':paginator, 'custom_range': custom_range}
    return render(request, 'projects/projects.html', context)

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
            return redirect('account')
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
            return redirect('account')
    return render(request, 'projects/project_form.html', context = {'form': form})

@login_required(login_url='login')
def deleteProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('account')
    return render(request, 'delete_object.html', context= {'project': project})
