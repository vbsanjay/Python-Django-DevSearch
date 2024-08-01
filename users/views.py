from django.shortcuts import render
from .models import Profile

def loginPage(request):
    return render(request, 'users/login_registers.html')

def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, 'users/profiles.html', context)


def userProfile(request, pk):
    userProfile = Profile.objects.get(id=pk)

    topSkills = userProfile.skill_set.exclude(description__exact="")
    otherSkills = userProfile.skill_set.filter(description="")

    context = {'userProfile': userProfile, 'topSkills': topSkills, 'otherSkills': otherSkills}
    return render(request, 'users/user-profile.html', context)