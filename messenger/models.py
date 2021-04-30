from django.db import models
from datetime import datetime

# Create your models here.
class Messenger(models.Model):
    id = models.AutoField(primary_key=True)
    bname = models.CharField(max_length=200)
    book_id = models.IntegerField()
    
    age = models.IntegerField(blank=True,default=20)
    
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length = 15)
    message = models.TextField(blank=True)
    contact_data = models.DateTimeField(default = datetime.now,blank = True)
    user_id = models.IntegerField(blank = True)


    def __str__(self):
        return self.name