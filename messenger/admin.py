from django.contrib import admin
from .models import Messenger


# Register your models here.
class MessengerAdmin(admin.ModelAdmin):
    list_display=('id','name','bname','book_id','email','phone','age')
    list_display_links = ('id','bname','name')
    search_fields = ('name','bname','email')
    list_per_page = 20

# Register your models here.
admin.site.register(Messenger,MessengerAdmin)