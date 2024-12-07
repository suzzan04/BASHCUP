from django.db import models

# Create your models here.

class products(models.Model):
    title = models.CharField(max_length=100)

    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField()

    def __str__(self):
        return self.title
    

class handicraftProduct(models.Model):
    title = models.CharField(max_length=100)

    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField()

    def __str__(self):
        return self.title