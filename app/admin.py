from django.contrib import admin
from .models import *
from .forms import *


@admin.register(Book)
class PersonAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class PersonAdmin(admin.ModelAdmin):
    pass

@admin.register(Shelf)
class PersonAdmin(admin.ModelAdmin):
    pass