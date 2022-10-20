from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Care)
class Careadmin(admin.ModelAdmin):
    list_display=['name']