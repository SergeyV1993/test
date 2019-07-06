from django.contrib import admin
from .models import *


@admin.register(Cars)
class CarsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Cars._meta.fields]

    class Meta:
        model = Cars
