from .models import Project, Tag
from django.db.models import Q

def searchProjects(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    
    tags = Tag.objects.filter(name__icontains=search_query)
    
    projectsList = Project.objects.distinct().filter(
        Q(title__icontains=search_query) |
        Q(description__icontains=search_query) |
        Q(owner__name__icontains=search_query) | # get into parent object(owner) check for attribut name in parent object
        Q(tags__in=tags) #searching for many to many fields
    )
    return projectsList, search_query