from django.contrib import admin
from .models import NewNews


# Register your models here.
@admin.register(NewNews)
class NewNewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title', 'content')
    list_per_page = 10
