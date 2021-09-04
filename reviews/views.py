from django.shortcuts import render

from .models import Book, Review
from .utils import average_rating


def index(request):
    name = "world"
    return render(request, "base.html", {"name": name})


def book_search(request):
    search_item = request.GET.get("search", "")
    return render(request, "search_results.html", {"search_item": search_item})


def welcome_view(request):
    books_quantity = Book.objects.count()
    return render(request, "base.html", {"books_quantity": books_quantity})


def book_list(request):
    books = Book.objects.all()                                      # query all books from table
    books_with_reviews = []
    for book in books:
        reviews = book.review_set.all()                             # get all reviews for each book
        if reviews:                                                 # if there're any reviews
            book_rating = average_rating(
                [review.rating for review in reviews]               # list comprehension
            )
            number_of_reviews = len(reviews)
        else:
            book_rating = None
            number_of_reviews = 0
        books_with_reviews.append(                                  # add a list of dictionaries
            {
                "book": book,
                "book_rating": book_rating,
                "number_of_reviews": number_of_reviews
            }
        )
    context = {
        "books_with_reviews": books_with_reviews
    }
    return render(request, "books_list.html", context)
