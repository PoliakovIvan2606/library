from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Book, Category
from .forms import PostBook
def index(request):
    context = {
        'books': Book.objects.all(),
        'categories': Category.objects.all()
    }
    return render(request, 'app/index.html', context)

def add_book(request):
    if request.method == 'POST':
        form = PostBook(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    context = {
        'form': PostBook(),
    }
    return render(request, 'app/add_book.html', context)