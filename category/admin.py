from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):

    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Category, CategoryAdmin)
