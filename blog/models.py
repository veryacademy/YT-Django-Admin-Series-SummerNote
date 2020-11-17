from django.db import models

class Post(models.Model):

    title = models.CharField(max_length=100)
    content = models.TextField(default=None, blank=True)

    def __str__(self):
        return self.title
