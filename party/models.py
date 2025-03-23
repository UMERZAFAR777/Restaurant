from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Party(models.Model):
    img = models.ImageField(upload_to='party/',)
    party_name = models.CharField(max_length=100)
    description = RichTextField()



    def __str__(self):
        return self.party_name
