# bookshelf/models.py

from django.db import models
class Author(models.Model):
    name = models.CharField(max_length=100)
    # Optional: add other author fields like birthdate, etc.

    def __str__(self):
        return self.name
    # Django automatically creates a primary key (id) for each model.

class Book(models.Model):
    title = models.CharField(max_length=200)
    # Establishes a many-to-one relationship with the Author model
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    summary = models.TextField(blank=True, null=True)
    isbn = models.CharField(max_length=13, unique=True, help_text='13 Character ISBN number')
    publication_date = models.DateField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    # Optional: add other fields like genre (using ManyToManyField or ForeignKey), availability, etc.

    def __str__(self):
        return self.title
       
   