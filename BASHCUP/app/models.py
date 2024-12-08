from django.db import models

# Create your models here.

class products(models.Model):
    title = models.CharField(max_length=100)

    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField()
    description = models.TextField(default="No description available.")
    def __str__(self):
        return self.title
    

    def delete(self, *args, **kwargs):
        # Delete the image file when the model instance is deleted
        if self.image:
            self.image.delete(save=False)
        super().delete(*args, **kwargs)



class handicraftProduct(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField()
    description = models.TextField(default="No description available.")

    def __str__(self):
        return self.title
    
    def delete(self, *args, **kwargs):
        # Delete the image file when the model instance is deleted
        if self.image:
            self.image.delete(save=False)
        super().delete(*args, **kwargs)



