from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic

from .models import Book, Author

# Create your views here.
class IndexView(generic.ListView):
    template_name='project/index.html'
    context_object_name='latest_book_list'

    def get_queryset(self):
        return Book.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model=Book
    template_name='project/detail.html'

class changeView(generic.DetailView):
    model=Book
    template_name='project/changes.html'
    
def index(request):
    latest_book_list=Book.objects.order_by('-pub_date')[:5]
    template=loader.get_template('project/index.html')
    context={'latest_book_list':latest_book_list,}
    return HttpResponse(template.render(context,request))

def detail(request, book_id):
    book=get_object_or_404(Book,pk=book_id)
    return render(request,'project/detail.html',{'book':book})

def change_book(request, book_id):
    book=get_object_or_404(Book,pk=book_id)
    book.book_name=book.book_name+' test'
    book.save()
    return HttpResponseRedirect(reverce('project:detail', args=(book_id,)))
