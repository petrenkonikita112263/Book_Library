from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer


@api_view(http_method_names=["GET"])
def first_api_view(request):
    number_books = Book.objects.count()
    return Response({"number_books": number_books})


@api_view(http_method_names=["GET"])
def all_books(request):
    books = Book.objects.all()
    book_serializer = BookSerializer(books, many=True)
    return Response(book_serializer.data)
