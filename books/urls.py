from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name='recommended'),
    path('available',views.available,name='available'),
    path('<int:book_id>',views.book,name='book'),
    path('search',views.search,name='search')
]
