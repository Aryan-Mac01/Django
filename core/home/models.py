from django.db import models

# Create your models here.

class Student(models.Model):
    #id = models.AutoField() --> ye default field hoti jo django khud se automatic add kardeta
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(null = True, blank = True)
    address = models.TextField()
    image = models.ImageField()
    file = models.FileField()
    document = models.FileField()


class Product(models.Model):
    pass