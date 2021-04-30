from django.contrib import admin
from .models import Seller


class SellerAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','phone','is_best')
    list_display_links = ('id','name')
    list_filter = ('name',)
    list_editable = ('is_best',)
    search_fields = ('name',)
    list_per_page = 10


# Register your models here.
admin.site.register(Seller,SellerAdmin)
