from django.contrib import admin
from web_site.models import Project


# Register your models here.

def make_published(modeladmin, request, queryset):
    queryset.update(status='p')

make_published.short_description = "Mark selected stories as published"

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    ordering = ['title']
    actions = [make_published]

admin.site.register(Project, ProjectAdmin)