from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .models import Book, Contributor
from .serializers import BookSerializer, ContributorSerializer


@api_view(http_method_names=["GET"])
def first_api_view(request):
    number_books = Book.objects.count()
    return Response({"number_books": number_books})


class AllBooks(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class ContributorView(generics.ListAPIView):
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer
