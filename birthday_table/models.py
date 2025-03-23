from django.db import models

# Create your models here.



class Birthday_table(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    date = models.DateField()
    time = models.TimeField()
    people = models.IntegerField()
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.date} at {self.time}"







