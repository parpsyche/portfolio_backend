from django.contrib import admin
from .models import Project, Tag, Category

admin.site.register(Project)
admin.site.register(Tag)
admin.site.register(Category)
