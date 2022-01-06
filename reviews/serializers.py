from rest_framework import serializers
from .models import Book, Publisher


class PublisherSerializer(serializers.Serializer):
    class Meta:
        model = Publisher
        fields = ["name", "website", "email"]


class BookSerializer(serializers.Serializer):
    class Meta:
        model = Book
        fields = ["title", "publication_date", "isbn", "publisher"]
