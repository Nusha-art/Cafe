from django.contrib import admin
from .models import *
@admin.register(menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'cost', 'category']
    search_fields = ['id', 'name']

@admin.register(gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['id', 'name']

@admin.register(team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['id', 'name']

@admin.register(vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['id', 'name']

@admin.register(reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'mark']
    search_fields = ['id', 'name']
# Register your models here.
