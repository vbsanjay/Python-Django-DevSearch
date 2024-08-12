from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Project, Tag
from .forms import ProjectForm, ReviewForm
from .utils import searchProjects, paginateProject

# Create your views here.
def projects(request):
    projectsList, search_query = searchProjects(request)
    results = 6
    custom_range, projectsList = paginateProject(request, projectsList, results)

    context = {'projects': projectsList, 'search_query': search_query, 
            'custom_range': custom_range}
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    projectObj = Project.objects.get(id = pk)
    form = ReviewForm()
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.project = projectObj
        review.owner = request.user.profile
        review.save()
        projectObj.getVoteCount # update project vore count
        messages.success(request, 'Your review successfully submitted')
        return redirect('project', pk=projectObj.id)

    context = {'project':projectObj, 'form': form}
    return render(request, 'projects/single-project.html', context)

@login_required(login_url='login')
def createProject(request):
    profile = request.user.profile
    form = ProjectForm()
    if request.method == 'POST':
        newtags = request.POST.get('newtags').replace(','," ").split()
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit = False) # return instance of current project
            project.owner = profile
            project.save()
            for tag in newtags:
                tag, created = Tag.objects.get_or_create(name=tag)
                project.tags.add(tag)
            return redirect('account')
    return render(request, 'projects/project_form.html', context = {'form': form})

@login_required(login_url='login')
def updateProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        newtags = request.POST.get('newtags').replace(','," ").split()
        form = ProjectForm(request.POST,request.FILES, instance=project)

        if form.is_valid():
            project = form.save()
            for tag in newtags:
                tag, created = Tag.objects.get_or_create(name=tag)
                project.tags.add(tag)
            return redirect('account')
        
    context = {'form': form, 'project': project}
    return render(request, 'projects/project_form.html', context)

@login_required(login_url='login')
def deleteProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('account')
    return render(request, 'delete_object.html', context= {'project': project})
