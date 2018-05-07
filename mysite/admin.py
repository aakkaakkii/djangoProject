from django.contrib import admin
from .models.models import Article

# Register your models here.


class AuthorAdmin(admin.ModelAdmin):
    admin.site.register(Article)
