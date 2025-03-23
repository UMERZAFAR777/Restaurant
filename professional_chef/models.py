from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Professional_Chef(models.Model):
    img = models.ImageField(upload_to='chef/',)
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = RichTextField()


    def __str__(self):
        return self.name
