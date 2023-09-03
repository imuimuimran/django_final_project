from django.db import models

class BookCatalog(models.Model):
    title = models.CharField(max_length=200, unique = True)
    slug = models.SlugField(max_length= 100, unique = True)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, unique=True)
    publication_date = models.DateTimeField(auto_now_add=True)
    genre = models.CharField(max_length=100)
    availability_status = models.BooleanField(default=True)
    no_of_books_available = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

