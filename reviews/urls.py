"""reviews URL Configuration"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views, api_views

router = DefaultRouter()
router.register(r"books", api_views.BookViewSet)
router.register(r"reviews", api_views.ReviewViewSet)

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
    path("api/", include((router.urls, "api"))),
    path("api/contributors/", api_views.ContributorView.as_view(), name="contributors"),
    path("api/login", api_views.Login.as_view(), name="login")
]
