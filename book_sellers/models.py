from django.db import models

# Create your models here.
class Seller(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to = 'photos/%Y/%m/%d')
    description = models.TextField(blank = True)
    phone = models.CharField(max_length = 20)
    email = models.CharField(max_length = 35)
    is_best =models.BooleanField(default = False)

    def __str__(self):
        return self.name
