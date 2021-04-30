from django.shortcuts import render,get_object_or_404
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from django.contrib import messages

from .models import Book

from messenger.models import Messenger

# Create your views here.
def index(request):

	detail = Messenger.objects.all().filter(user_id=request.user.id)
	
	# user_id =[]
	# for i in detail.values_list('user_id'):
	# 	user_id.append(i[0])

	book_id = []
	for j in detail.values_list('book_id'):
		book_id.append(j[0])

	genre=[]
	for x in book_id:
		ans = Book.objects.all().filter(id=x)
		if ans.values_list('genre1')[0][0]:
			genre.append(ans.values_list('genre1')[0][0])
		
		if ans.values_list('genre2')[0][0]:
			genre.append(ans.values_list('genre2')[0][0])
		
		if ans.values_list('genre3')[0][0]:
			genre.append(ans.values_list('genre3')[0][0])
		
	# id_bk = detail.values_list('book_id')
	# Book.objects.all().filter(id__in=id_bk)
	# query_list = Bookobjects.all().filter(bname__icontains=book_name)

	books1 = Book.objects.all().filter(genre1__in=genre)
	books2 = Book.objects.all().filter(genre2__in=genre)
	books3 = Book.objects.all().filter(genre3__in=genre)

	books = (books1 | books2 | books3).distinct()
 	
	
	

	paginator = Paginator(books,9)
	page = request.GET.get('page')
	paged_books = paginator.get_page(page)
	context ={
		'books' : paged_books,
	}

	context ={
		'books' : books
	}
	
	if books.count()==0:
		books = Book.objects.all()
		paginator = Paginator(books,9)
		page = request.GET.get('page')
		paged_books = paginator.get_page(page)
		context ={
			'books' : paged_books
		}
		return render(request,'books/available.html',context)
		
	else:
		return render(request,'books/recommended.html',context)


def available(request):
	books = Book.objects.all()
	paginator = Paginator(books,9)
	page = request.GET.get('page')
	paged_books = paginator.get_page(page)
	context ={
		'books' : paged_books
	}
	return render(request,'books/available.html',context)


def book(request,book_id):
	book = get_object_or_404(Book,pk=book_id)
	
	context = {
		'book' : book
	}
	return render(request,'books/book.html',context)


def search(request):
	query_list = Book.objects.all().order_by('-list_date')

	if 'book_name' in request.GET:
		book_name = request.GET['book_name']
		if book_name:
			query_list = query_list.filter(bname__icontains=book_name)

	if 'isbn' in request.GET:
		isbn = request.GET['isbn']
		# if isbn:
		# 	query_list = query_list.filter(isbn__icontains=isbn)

	context = {
		'books' : query_list,
		'book_name' : book_name,
		'isbn' : isbn,
		'values' : request.GET
	}
	return render(request,'books/search.html',context)