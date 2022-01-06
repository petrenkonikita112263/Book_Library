"""reviews URL Configuration"""

from django.urls import path

from . import views, api_views

urlpatterns = [
    path("", views.welcome_view, name="welcome_view"),
    path("books/", views.book_list, name="book_list"),
    path("books/<int:book_id>", views.get_book_detail, name="get_book_detail"),
    path("publisher/<int:publisher_id>", views.publisher_edit, name="publisher_edit"),
    path("publisher/new/", views.publisher_edit, name="publisher_create"),
    path("books/<int:book_id>/reviews/<int:review_id>", views.review_edit, name="review_edit"),
    path("books/<int:book_id>/review/new", views.review_edit, name="review_create"),
    path("books/<int:book_id>/media/", views.book_media, name="book_media"),
    path("api/first_api_view/", api_views.first_api_view),
    path("api/all_books/", api_views.AllBooks.as_view(), name="all_books")
]
