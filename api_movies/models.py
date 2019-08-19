from django.db import models
from django.conf import settings

class Movie(models.Model):

    id = models.AutoField(primary_key=True)
    title = models.TextField()
    imdbid = models.TextField()
