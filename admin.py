from django.contrib import admin


class BookrAdminSite(admin.AdminSite):
    """Custom admin site for Bookr application."""
    title_header = "Bookr Admin"
    site_header = "Bookr administration"
    index_title = "Book site admin"
