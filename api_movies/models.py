from django.db import models
from django.conf import settings

class Movie(models.Model):

#    class Meta:
#        app_label = 'api_movies"'

    id = models.AutoField(primary_key=True)
    title = models.TextField()
    imdbid = models.TextField()
