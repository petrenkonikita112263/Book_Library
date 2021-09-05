from admin import BookrAdminSite
from reviews.models import Publisher, Book, Contributor, \
    BookContributor, Review

admin_site = BookrAdminSite(name="bookr")

"""Registrate models for AdminSite."""
admin_site.register(Publisher)
admin_site.register(Book)
admin_site.register(Contributor)
admin_site.register(BookContributor)
admin_site.register(Review)
