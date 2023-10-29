from django.contrib import admin
from .models import Book, Category


@admin.register(Book)
class PersonAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class PersonAdmin(admin.ModelAdmin):
    pass