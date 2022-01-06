from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book


@api_view(http_method_names=["GET"])
def first_api_view(request):
    number_books = Book.objects.count()
    return Response({"number_books": number_books})
