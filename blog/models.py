from django.db import models
from django.core.urlresolvers import reverse

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200, unique=True)
    pub_date = models.DateTimeField('Date published')
    mod_date = models.DateTimeField('Date last modified')
    hidden = models.BooleanField(default=True) 
    body = models.TextField()

    def __str__(self):
        return self.title

