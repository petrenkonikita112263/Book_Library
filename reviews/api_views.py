from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer


@api_view(http_method_names=["GET"])
def first_api_view(request):
    number_books = Book.objects.count()
    return Response({"number_books": number_books})


class AllBooks(generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
