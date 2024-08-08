from .models import Project, Tag
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def paginateProject(request, projectsList, results):

    page = request.GET.get('page')
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

    return custom_range, projectsList

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