from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    email = models.EmailField()
    description = models.TextField()

    def __str__(self):
        return self.name +"--"+ self.title