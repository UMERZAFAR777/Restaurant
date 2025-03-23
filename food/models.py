from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class Section(models.Model):
    name = models.CharField(max_length= 100)

    def __str__(self):
        return self.name
    

class Food(models.Model):
    sec_name = models.ForeignKey(Section,on_delete=models.DO_NOTHING)
    img = models.ImageField(upload_to = "food/")
    food_name = models.CharField(max_length=200)
    price = models.IntegerField()
    decription = RichTextField()


    def __str__(self):
        return self.sec_name.name +"--"+ self.food_name
        



