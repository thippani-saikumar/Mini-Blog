from django.contrib import admin
from .models import post

# Register your models here.
@admin.register(post)
class postModelAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "description"]
    