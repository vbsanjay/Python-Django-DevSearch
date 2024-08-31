from django.contrib import admin

# Register your models here.
from .models import Project, Review, Tag

# By registering these models, you’ll be able to add, edit, and delete instances of these models from the Django admin dashboard. 
admin.site.register(Project)
admin.site.register(Review)
admin.site.register(Tag)