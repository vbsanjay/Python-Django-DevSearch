from django.http import HttpResponse
from django.shortcuts import render

projectsList = [
    {
        'id':'1',
        'title': 'Ecommerce website',
        'description': 'Costumer can buy products here'
    },
    {
        'id':'2',
        'title': 'Portfolio website',
        'description': 'This is the project where i built my portfolio'
    },
    {
        'id':'3',
        'title': 'Social network',
        'description': 'A app where people can interact with eachother'
    },
]

# Create your views here.
def projects(request):
    msg = "Below are the list of all the projects"
    number = 10
    return render(request, 'projects/projects.html', context={'message':msg, 'number':number, 'projects': projectsList})

def project(request, pk):
    projectObj = None
    for project in projectsList:
        if project['id'] == pk:
            projectObj = project
    return render(request, 'projects/single-project.html', context = {'project':projectObj})