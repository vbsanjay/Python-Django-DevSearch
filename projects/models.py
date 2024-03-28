from django.db import models
import uuid

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField(null = True, blank = True)
    demo_link = models.CharField(max_length =2000, null = True, blank = True)
    source_line = models.CharField(max_length =2000, null = True, blank = True)
    created = models.DateTimeField(auto_now_add= True)
    id = models.UUIDField(primary_key = True, editable = False, unique = True, default=uuid.uuid4)

    def __str__(self):
        return self.title