from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from .models import *
from .forms import *
def index(request, cat=None, shelf=None):
    if cat:
        books = Book.objects.filter(category_id=cat, user_id=request.user.id)
    elif shelf:
        books = Book.objects.filter(shelf_id=shelf, user_id=request.user.id)
    else:
        books = Book.objects.filter(user_id=request.user.id)
    context = {
        'books': books,
        'categories': Category.objects.all(),
        'shelfs': Shelf.objects.filter(user_id=request.user.id)
    }
    return render(request, 'app/index.html', context)

@login_required
def add_book(request):
    if request.method == 'POST':
        form = PostBook(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = PostBook()
    context = {
        'form': form,
    }
    return render(request, 'app/add_book.html', context)

def add_shelf(request):
    books = Book.objects.filter(shelf_id=None, user_id=request.user.id)
    print(request.POST)
    if request.method == "POST":
        list_post = list(request.POST)
        shelf = Shelf.objects.create(name=request.POST[list_post[1]], user_id=request.user.id)
        for name, chek in list(request.POST.items())[2:]:
            book = Book.objects.get(name=name)
            book.shelf_id = shelf.id
            book.save()
        return HttpResponseRedirect(reverse('index'))
    return render(request, 'app/shelf.html', {'books': books})


class LoginUser(LoginView):
    form_class = UserLoginForm
    template_name = 'app/login.html'

class RegisterUser(CreateView):
    form_class = UserRegistrationForm
    template_name = 'app/registration.html'
    success_url = reverse_lazy('login')
def logout(request):
        auth.logout(request)
        return HttpResponseRedirect(reverse('index'))