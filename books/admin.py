from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display=('id','bname','is_published','price','list_date','seller')
    list_display_links = ('id','bname')
    list_filter = ('seller',)
    list_editable = ('is_published',)
    search_fields = ('description','price','bname')
    list_per_page = 20

# Register your models here.
admin.site.register(Book,BookAdmin)
