from django.shortcuts import render
from django.http import HttpResponse
from .models import Book


def index(request):
    name = "world"
    return render(request, "base.html", {"name": name})


def book_search(request):
    search_item = request.GET.get("search", "")
    return render(request, "search_results.html", {"search_item": search_item})


def welcome_view(request):
    message = f"<html><h1>Welcome to Bookr application!</h1>" \
              f"<p>{Book.objects.count()} books and counting!</p></html>"
    return HttpResponse(message)
