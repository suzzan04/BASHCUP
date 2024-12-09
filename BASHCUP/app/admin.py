from django.contrib import admin
from .models import products, handicraftProduct, specialCoffe, specialHandicraft


class Productcoffee(admin.ModelAdmin):
    list_display = ('title', 'price', 'image', 'description')


class specialCoffeProduct(admin.ModelAdmin):
    list_display = ('image',)


class Producthandicraft(admin.ModelAdmin):
    list_display = ('title', 'price', 'image', 'description')
    
class specialHandiProduct(admin.ModelAdmin):
    list_display = ('image',)


admin.site.register(products, Productcoffee)
admin.site.register(handicraftProduct, Producthandicraft)
admin.site.register(specialCoffe, specialCoffeProduct)
admin.site.register(specialHandicraft, specialHandiProduct)
