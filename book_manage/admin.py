from django.contrib import admin
from .models import BookCatalog 
# Register your models here.

class CatalogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('title',)}
    list_display = ('title', 'slug')
    
admin.site.register(BookCatalog, CatalogAdmin)


class BookDetailAdmin(admin.ModelAdmin): 
     list_display = ['title', 'authore', 'isbn', 'publication_date', 'genre', 'availability_status', 'no_of_books_available']
     
     prepopulated_fields = {'slug' : ('title',)}
     
# admin.site.register(BookCatalog, BookDetailAdmin)