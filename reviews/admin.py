from django.contrib.admin import AdminSite
from reviews.models import Publisher, Book, Contributor, \
    BookContributor, Review


class BookrAdminSite(AdminSite):
    """Custom admin site for Bookr application."""
    title_header = "Bookr Admin"
    site_header = "Bookr administration"
    index_title = "Book site admin"


admin_site = BookrAdminSite(name="bookr")

"""Registrate models for AdminSite."""
admin_site.register(Publisher)
admin_site.register(Book)
admin_site.register(Contributor)
admin_site.register(BookContributor)
admin_site.register(Review)
