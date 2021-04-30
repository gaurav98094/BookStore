from django.shortcuts import render
from django.http import HttpResponse

from books.models import Book

# Create your views here.
def index(request):
	books = Book.objects.order_by('-number_of_enquiry')[:6]    #.filter(is_published = True)

	context = {
		'books' : books
	}		

	return render(request,'pages/index.html', context)

def about(request):
	return render(request,'pages/about.html')

def recommended(request):
	return render(request,'pages/recommended.html')