from djongo import models

# Create your models here.

class Start(models.Model):
    entry = models.CharField(max_length=255)
    is_completed = models.BooleanField(default=False)