from django.db import models

# Create your models here.
#Servicios

class Services(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField() 

    def __str__(self):
        return self.name

<<<<<<< HEAD
#python .\manage.py makemigrations



=======
class Insumo (models.Model):
>>>>>>> 7a41d43ae65f9255b615a093fb968a560a2c6012

    name = models.CharField(max_length= 120)
    price = models.IntegerField()
    Image = models.ImageField(upload_to="insumos", null=True)
    Description =models.TextField()
    Stock = models.IntegerField()

    def __str__(self):
        return self.name


class Slider(models.Model):
<<<<<<< HEAD
    name = models.IntegerField() 
    image = models.ImageField(upload_to="sliders", null=True)

    def __init__(self):
        return self.name

class Gallery(models.Model):
    name = models.IntegerField() 
    image = models.ImageField(upload_to="gallery", null=True)

    def __init__(self):
=======
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="sliders", null=True)

    def __str__(self):
        return self.name


class Gallery(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="gallery", null=True)

    def __str__(self):
>>>>>>> b63764345592fb212ac82a954a05ce249fe0792f
        return self.name