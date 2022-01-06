from rest_framework import serializers
from .models import Book, Publisher, Contributor


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ["name", "website", "email"]


class BookSerializer(serializers.ModelSerializer):
    publisher = PublisherSerializer()

    class Meta:
        model = Book
        fields = ["title", "publication_date", "isbn", "publisher"]


class ContributionSerializer(serializers.ModelSerializer):
    book = BookSerializer()

    class Meta:
        model = Contributor
        fields = ["book", "role"]
