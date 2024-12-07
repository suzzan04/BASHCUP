from django.contrib import admin
from .models import products, handicraftProduct
# Register your models here.


class Productcoffee(admin.ModelAdmin):
    list_display = ('title', 'price', 'image')


class Producthandicraft(admin.ModelAdmin):
    list_display = ('title', 'price', 'image')

admin.site.register(products, Productcoffee)
admin.site.register(handicraftProduct, Producthandicraft)