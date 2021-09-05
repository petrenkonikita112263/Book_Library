from django.contrib import admin
from reviews.models import Publisher, Book, Contributor, \
    BookContributor, Review

"""Registrate models for AdminSite."""
admin.site.register(Publisher)
admin.site.register(Book)
admin.site.register(Contributor)
admin.site.register(BookContributor)
admin.site.register(Review)
