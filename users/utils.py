from .models import Profile, Skill
from django.db.models import Q

def searchProfiles(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    
    skills = Skill.objects.filter(name__icontains=search_query)
    
    # name__icontains=search_query, short_intro__icontains=search_query line represent both name and short intro should contain letter we search for
    # from django.db.models import Q this will help us to return data if search value is present either in name or short intrp
    profiles = Profile.objects.distinct().filter(Q(name__icontains=search_query) | 
                                      Q(short_intro__icontains=search_query) |
                                      Q(skill__in=skills)) # skill__in=skills, this syntax for child object
    
    
    return profiles, search_query