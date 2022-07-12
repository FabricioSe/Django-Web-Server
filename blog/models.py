from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models/tables here.

class Post(models.Model):

    title = models.CharField(max_length = 100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    ## Overriding methods
    def __str__(self):
        return self.title

## Make migrations --> 0001_initial.py will be generated
## Then to integrate the new model in the database you need to migrate
## migrate --> ok