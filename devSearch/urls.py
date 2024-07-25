from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls), # username: vbsanjay password_hint: starts with H and ends with 2
    path('', include('projects.urls')),
]
