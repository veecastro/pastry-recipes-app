from django.contrib import admin

from main_app.models import Pastryrecipe, Photo, Category
# Register your models here.
admin.site.register(Pastryrecipe)
admin.site.register(Photo)
admin.site.register(Category)
