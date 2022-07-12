from django.db import models

# Post object model
class Post(models.Model):
    def __str__(self):
        return self.title

    title = models.CharField(verbose_name="Post title" ,max_length=100)
    contents = models.TextField(verbose_name="Post contents")
    posted_at = models.DateTimeField(verbose_name="Posted at")