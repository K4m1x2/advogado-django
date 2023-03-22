from django.contrib import admin
from .models import Category, Article

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    ...

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    ...

admin.site.register(Category, CategoryAdmin)
