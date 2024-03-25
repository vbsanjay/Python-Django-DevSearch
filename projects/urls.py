from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('helloName/<str:name>', views.helloName, name='helloName'),
]