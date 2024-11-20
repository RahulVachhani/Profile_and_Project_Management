from django.contrib import admin
from .models import Project, Review, Tag

# Register your models here.

class show_projects(admin.ModelAdmin):
    list_display = ['title', 'discription', 'id']

class show_review(admin.ModelAdmin):
    list_display = ['owner', 'project']

class show_tags(admin.ModelAdmin):
    list_display = ['name', 'created']

admin.site.register(Project, show_projects)
admin.site.register(Review,show_review)
admin.site.register(Tag, show_tags)

