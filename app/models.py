from django.db import models

# Create your models here.
#Servicios

class Services(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField() 

    def __str__(self):
        return self.name

class Insumo (models.Model):

    name = models.CharField(max_length= 120)
    price = models.IntegerField()
    Image = models.ImageField(upload_to="insumos", null=True)
    Description =models.TextField()
    Stock = models.IntegerField()

    def __str__(self):
        return self.name


class Slider(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="sliders", null=True)

    def __str__(self):
        return self.name


class Gallery(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="gallery", null=True)

    def __str__(self):
        return self.name