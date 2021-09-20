"""reviews URL Configuration"""

from django.urls import path

from . import views

urlpatterns = [
    path("", views.welcome_view, name="welcome_view"),
    path("books/", views.book_list, name="book_list"),
    path("books/<int:book_id>", views.get_book_detail, name="get_book_detail"),
    path("publisher/<int:publisher_id>", views.publisher_edit, name="publisher_edit"),
    path("publisher/new/", views.publisher_edit, name="publisher_create")
]
