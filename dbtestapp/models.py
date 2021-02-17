from django.db import models

# Create your models here.

class book_master(models.Model):
    bookid=models.IntegerField(primary_key=True)
    bookname=models.CharField(max_length=20)
    bookprice=models.IntegerField()