from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import generics, viewsets
from .models import Book, Contributor, Review
from .serializers import BookSerializer, ContributorSerializer, ReviewSerializer


@api_view(http_method_names=["GET"])
def first_api_view(request):
    number_books = Book.objects.count()
    return Response({"number_books": number_books})


class BookViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class ContributorView(generics.ListAPIView):
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer


class ReviewViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Review.objects.order_by("-date_created")
    serializer_class = ReviewSerializer
    pagination_class = LimitOffsetPagination
    authentication_classes = []
