from django.contrib import admin
from .models import Book, Author

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    fields=['pub_date','book_name']

admin.site.register(Book)
admin.site.register(Author)
