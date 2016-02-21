from django.db import models
import django.utils.timezone as timezone
# Create your models here.
class tubi(models.Model):
    name = models.CharField(max_length=30)
    content = models.CharField(max_length=90)
    time = models.DateTimeField(default=timezone.now)
