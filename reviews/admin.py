from django.contrib import admin
from admin import BookAdmin, ReviewAdmin
from reviews.models import Publisher, Book, Contributor, \
    BookContributor, Review

"""Registrate models for AdminSite."""
admin.site.register(Publisher)
admin.site.register(Book, BookAdmin)
admin.site.register(Contributor)
admin.site.register(BookContributor)
admin.site.register(Review, ReviewAdmin)
