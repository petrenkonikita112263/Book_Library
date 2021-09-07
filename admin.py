from django.contrib import admin


class BookrAdminSite(admin.AdminSite):
    """Custom admin site for Bookr application."""
    title_header = "Bookr Admin"
    site_header = "Bookr administration"
    index_title = "Book site admin"


class BookAdmin(admin.ModelAdmin):
    """Customise the book displaying in admin site."""
    list_display = ("title", "isbn")
    list_filter = ("publisher", "publication_date")
    date_hierarchy = "publication_date"
    search_fields = ("title", "isbn", "publisher__name__startswith")


class ReviewAdmin(admin.ModelAdmin):
    exclude = ("date_edited",)
    fieldsets = (
        (
            "Linkage", {"fields": ("creator", "book")}
        ),
        (
            "Review content", {"fields": ("content", "rating")}
        )
    )
