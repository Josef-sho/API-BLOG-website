from djongo import models

class BlogPost(models.Model):
    title = models.CharField(max_length=250, unique=True)
    subtitle = models.CharField(max_length=250)
    date = models.DateField()
    body = models.TextField()
    author = models.CharField(max_length=250)
    img_url = models.URLField()
    