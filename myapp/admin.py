from django.contrib import admin
from .models import Property, PropertyCategory, PropertySector, PropertyFacing, PropertyImage, Province, Country, City, Advertisement

# Register your models here.

admin.site.register(Property)
admin.site.register(PropertyCategory)
admin.site.register(PropertySector)
admin.site.register(PropertyFacing)
admin.site.register(PropertyImage)
admin.site.register(Country)
admin.site.register(Province)
admin.site.register(City)
admin.site.register(Advertisement)

