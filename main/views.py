from django.shortcuts import render
from .models import Task
from .models import Book


def index(request):
    tasks = Task.objects.all()
    return render(request, 'main/index.html', {'title':'Главная строница сайта', 'tasks': tasks})


def les(request):
    books = Book.objects.all()
    return render(request, 'main/les.html', {'title':'Книги', 'books': books})


def about(request):
    return render(request, 'main/about.html')


def lesson_1(request):
    return render(request, 'main/lesson_1.html')


