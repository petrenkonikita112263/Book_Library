from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from .models import Book, Contributor, Publisher
from .utils import average_rating
from .forms import SearchForm, PublisherForm


def welcome_view(request):
    books_quantity = Book.objects.count()
    return render(request, "reviews/base.html", {"books_quantity": books_quantity})


def book_search(request):
    search_item = request.GET.get("search", "")
    form = SearchForm(request.GET)
    books = set()
    if form.is_valid() and form.cleaned_data["search"]:
        search = form.cleaned_data["search"]
        search_in = form.cleaned_data.get("search_in") or "title"
        if search_in == "title":
            books = Book.objects.filter(title__icontains=search)
        else:
            first_names = Contributor.objects.filter(first_names__icontains=search)
            for contributor in first_names:
                for book in contributor.book_set.all():
                    books.add(book)
            last_names = Contributor.objects.filter(last_names__icontains=search)
            for contributor in last_names:
                for book in contributor.book_set.all():
                    books.add(book)
    return render(request, "reviews/search_results.html", {
        "form": form,
        "search_item": search_item,
        "books": books
    })


def book_list(request):
    """Lists all the books from Book table. Each book has own list of reviews.
    Based on this list finds the average rating. Created the list of dictionaries
    to display the information on html page."""
    books = Book.objects.all()
    books_with_reviews = []
    for book in books:
        reviews = book.review_set.all()
        if reviews:
            book_rating = average_rating(
                [review.rating for review in reviews]
            )
            number_of_reviews = len(reviews)
        else:
            book_rating = None
            number_of_reviews = 0
        books_with_reviews.append(
            {
                "book": book,
                "book_rating": book_rating,
                "number_of_reviews": number_of_reviews
            }
        )
    context = {
        "books_with_reviews": books_with_reviews
    }
    return render(request, "reviews/books_list.html", context)


def get_book_detail(request, book_id: int):
    """Retrieves book object by its primary, for that book all the views
    were collected. Calculates the average rating for the book based on reviews.
    Created the dictionary fro displaying all this info in html page."""
    book = get_object_or_404(Book, pk=book_id)
    reviews = book.review_set.all()
    if reviews:
        book_rating = average_rating(
            [review.rating for review in reviews]
        )
        context = {
            "book": book,
            "book_rating": book_rating,
            "reviews": reviews
        }
    else:
        context = {
            "book": book,
            "book_rating": None,
            "reviews": None
        }
    return render(request, "reviews/book_details.html", context)
