from django.db import models
from datetime import datetime

from book_sellers.models import Seller


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    seller = models.ForeignKey(Seller,on_delete = models.DO_NOTHING)
    bname = models.CharField(max_length=100)
    isbn = models.CharField(max_length=40,blank=True)
    writerName = models.CharField(max_length=100)


    # cho=(
    #     ('action','Action'),
    #     ('adventure','Advnture'),
    #     ('history','History'),
    #     ('children','Children'),
    #     ('comic','Comic'),
    #     ('Magazine','magazine'),
    #     ('crime','Crime'),
    #     ('fantasy','Fantasy'),
    #     ('mystery','Mystery'),
    #     ('romance','Ronamce'),
    #     ('suspense','Suspense'),
    #     ('adult','Adult')

    # )
    # genres = models.CharField(max_length=100,choices=cho)

    genre1 = models.CharField(blank=True,max_length=32,choices=[("Motivational","Motivational"),("Fiction","Fiction"),("Business","Business"),("Children","Children"),("Health","Health"),("Story","Story"),("Novel","Novel"),("Fantasy","fantasy"),('Comic','Comic'),('Ronamce','Ronamce'),('Adventure','Adventure'),("Science","Science")],)
    genre2 = models.CharField(blank=True,max_length=32,choices=[("Motivational","Motivational"),("Fiction","Fiction"),("Business","Business"),("Children","Children"),("Health","Health"),("Story","Story"),("Novel","Novel"),("Fantasy","fantasy"),('Comic','Comic'),('Ronamce','Ronamce'),('Adventure','Adventure'),("Science","Science")],)
    genre3 = models.CharField(blank=True,max_length=32,choices=[("Motivational","Motivational"),("Fiction","Fiction"),("Business","Business"),("Children","Children"),("Health","Health"),("Story","Story"),("Novel","Novel"),("Fantasy","fantasy"),('Comic','Comic'),('Ronamce','Ronamce'),('Adventure','Adventure'),("Science","Science")],)
    
    
    price = models.IntegerField()   

    number_of_enquiry = models.IntegerField(default=0) 
    
    description = models.CharField(max_length=1000)
    photo_main = models.ImageField(upload_to = 'photos/%Y/%m/%d/')
    list_date = models.DateTimeField(default = datetime.now(),blank = True)

    is_published = models.BooleanField(default = True)

    def __str__(self):
        return self.bname
    