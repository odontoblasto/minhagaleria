from django.contrib import admin

# Register your models here.

from .models import CategoryModel, PhotoModel, ProfileModel

admin.site.register(CategoryModel)
admin.site.register(PhotoModel)
admin.site.register(ProfileModel)
