from django.contrib.auth.decorators import user_passes_test, login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.utils import timezone
from django.core.files.images import ImageFile

from PIL import Image
from io import BytesIO

from .models import Book, Contributor, Publisher, Review
from .utils import average_rating
from .forms import SearchForm, PublisherForm, ReviewForm, BookMediaForm


def welcome_view(request):
    books_quantity = Book.objects.count()
    return render(request, "reviews/base.html", {"books_quantity": books_quantity})


def book_search(request):
    search_item = request.GET.get("search", "")
    search_history = request.session.get("search_history", [])
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
        if request.user.is_authenticated:
            search_history.append([search_in, search])
            request.session["search_history"] = search_history
    elif search_history:
        initial = dict(
            search=search_item,
            search_in=search_history[-1][0]
        )
        form = SearchForm(initial=initial)
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
    if request.user.is_authenticated:
        max_viewed_books_length = 10
        viewed_books = request.session.get("viewed_books", [])
        viewed_book = [book.id, book.title]
        if viewed_book in viewed_books:
            viewed_books.pop(viewed_books.index(viewed_book))
        viewed_books.insert(0, viewed_book)
        viewed_books = viewed_books[:max_viewed_books_length]
        request.session["viewed_books"] = viewed_books
    return render(request, "reviews/book_details.html", context)


def is_staff_user(user):
    return user.is_staff


@user_passes_test(is_staff_user)
def publisher_edit(request, publisher_id=None):
    """View based function that edits the existed publisher by id or created the new one
    if the id was not sent."""
    if publisher_id is not None:
        publisher = get_object_or_404(Publisher, pk=publisher_id)
    else:
        publisher = None
    if request.method == "POST":
        form = PublisherForm(request.POST, instance=publisher)
        if form.is_valid():
            updated_publisher = form.save()
            if publisher is None:
                messages.success(request, f"Publisher {updated_publisher} was created.")
            else:
                messages.success(request, f"Publisher {updated_publisher} was updated.")
            return redirect("publisher_edit", updated_publisher.pk)
    else:
        form = PublisherForm(instance=publisher)
    return render(request, "reviews/instance_form.html", {
        "form": form,
        "instance": publisher,
        "model_type": "Publisher"
    })


@login_required
def review_edit(request, book_id, review_id=None):
    """View based function that edits the existed review for the book
    or assign new to the fetch book."""
    book = get_object_or_404(Book, pk=book_id)
    if review_id is not None:
        review = get_object_or_404(Review, book_id=book_id, pk=review_id)
        user = request.user
        if not user.is_staff and review.creator.id != user.id:
            raise PermissionDenied
    else:
        review = None
    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            updated_review = form.save(commit=False)
            updated_review.book = book
            if review is None:
                messages.success(request, f"Review for the {book} was created.")
            else:
                updated_review.date_edited = timezone.now()
                messages.success(request, f"Review for the {book} was updated.")
            updated_review.save()
            redirect("get_book_detail", book.pk)
    else:
        form = ReviewForm(instance=review)
    return render(request, "reviews/instance_form.html", {
        "form": form,
        "instance": review,
        "model_type": "Review",
        "related_instance": book,
        "related_model_type": Book
    })


@login_required
def book_media(request, book_id):
    """View based function that allow user to add media to the existed book."""
    book = get_object_or_404(Book, pk=book_id)
    if request.method == "POST":
        form = BookMediaForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            book = form.save(commit=False)
            cover = form.cleaned_data.get("cover")
            if cover:
                image = Image.open(cover)
                image.thumbnail((300, 300))
                image_data = BytesIO()
                image.save(fp=image_data, format=cover.image.format)
                image_file = ImageFile(image_data)
                book.cover.save(cover.name, image_file)
            book.save()
            messages.success(request, f"Book {book} was updated.")
            return redirect("get_book_detail", book.pk)
    else:
        form = BookMediaForm(instance=book)
    return render(
        request, "reviews/instance_form.html", {
            "form": form,
            "instance": book,
            "model_type": "Book",
            "is_file_upload": True
        }
    )
