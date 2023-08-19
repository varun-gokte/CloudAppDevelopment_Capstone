from django.contrib import admin
from .models import CarMake,carModel


# Register your models here.

# CarModelInline class

# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    fields = ['make', 'name', 'dealerId', 'type', 'year']


admin.site.register(CarMake)
admin.site.register(carModel, CarModelAdmin)

# CarMakeAdmin class with CarModelInline

# Register models here
