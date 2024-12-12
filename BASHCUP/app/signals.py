# signals.py
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from .models import products, handicraftProduct , specialCoffe , specialHandicraft,landingBanners
import os

# This function will run before a product or handicraftProduct is deleted
@receiver(pre_delete, sender=products)
@receiver(pre_delete, sender=handicraftProduct)
@receiver(pre_delete, sender=specialCoffe)
@receiver(pre_delete, sender=specialHandicraft)
@receiver(pre_delete, sender=landingBanners)
def delete_image_on_object_delete(sender, instance, **kwargs):
    if instance.image:  # Check if the instance has an image
        try:
            # Attempt to delete the image file from the media directory
            os.remove(instance.image.path)
        except Exception as e:
            print(f"Error deleting file: {e}")
