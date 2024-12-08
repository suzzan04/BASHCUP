from django.contrib import admin
from .models import products, handicraftProduct


class Productcoffee(admin.ModelAdmin):
    list_display = ('title', 'price', 'image', 'description')


class ProductSpecialcoffee(admin.ModelAdmin):
    list_display = ('image',)


class Producthandicraft(admin.ModelAdmin):
    list_display = ('title', 'price', 'image', 'description')
    
class ProductSpecialHandi(admin.ModelAdmin):
    list_display = ('image',)


admin.site.register(products, Productcoffee)

admin.site.register(handicraftProduct, Producthandicraft)
