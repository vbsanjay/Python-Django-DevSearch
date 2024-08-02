from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User

def loginUser(request):

    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            print('user name does not exist')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # login function helps to generate session id
            # when logged into our applicatio django admin also logged in
            login(request, user)
            return redirect('profiles')
        else:
            print('username or password is incorrect')

    return render(request, 'users/login_registers.html')

def logoutUser(request):
    logout(request)
    return redirect('login')

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