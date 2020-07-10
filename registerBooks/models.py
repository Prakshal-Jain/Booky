from django.db import models

# Create your models here.
class register_book(models.Model):
    Book_Name = models.CharField(max_length=300)
    book_image = models.ImageField(blank=True)
    author = models.CharField(blank=True, max_length=300)
    date = models.DateTimeField(blank=False)
    location = models.TextField(blank=False)
    description = models.TextField(blank=False)
    price = models.DecimalField(max_digits=20, decimal_places=2)