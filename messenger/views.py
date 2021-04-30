from django.shortcuts import render,redirect
from django.contrib import messages

from django.db.models import F

from .models import Messenger

from books.models import Book

from django.core.mail import send_mail

# Create your views here.
def contact(request):
    if request.method=='POST':
        book_id = request.POST['book_id']
        user_id = request.POST['user_id']
        seller_email = request.POST['seller_email']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        bname = bname = request.POST['bname']
        age = request.POST['age']


        Book.objects.filter(id = book_id).update(number_of_enquiry=F("number_of_enquiry") + 1)


        # Check if user have made entry for same book
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Messenger.objects.all().filter(book_id=book_id,user_id=user_id)

            if has_contacted:
                messages.error(request,'Your request Was Already Made For this Book')
                return redirect('/books/'+book_id)


            contact = Messenger(bname = bname, book_id =book_id,
                            name = name,email = email,phone = phone, message =message,
                            user_id = user_id,age=age)    
        
            contact.save()

            # send mail
            send_mail(
                'Book Inquiry',
                'There is an request for the book named '+bname +' Please check it.',
                'gaurav.kandel@science.christuniversity.in',
                [seller_email],
                fail_silently=False
            )

            messages.success(request,' Request Sumitted Sucessfully')
        else:
            messages.error(request,'Resister Yourself First')

        return redirect('/books/'+book_id)


