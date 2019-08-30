from django.db import models

# Create your models here.
class Book(models.Model):
    author=models.ForeignKey('Author', on_delete=models.CASCADE)
    book_name=models.CharField(max_length=200)
    pub_date=models.DateTimeField('Year of issue')
    edition=models.CharField(max_length=200)
    genre=models.CharField(max_length=100)
    def __str__(self):
        return self.book_name

class Author(models.Model):
    author_name=models.CharField(max_length=100)
    country_of_birth=models.CharField(max_length=50)
    year_of_birth=models.CharField(max_length=15)
    def __str__(self):
        return self.author_name
