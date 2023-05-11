from django.db import models

# Create your models here.
class Songs(models.Model):
    # id field is added automatically.
    # Each field is specified as a class attribute, 
    # and each attribute maps to a database column.
    title = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=200, blank=False, default='')
    published = models.BooleanField(default=False)