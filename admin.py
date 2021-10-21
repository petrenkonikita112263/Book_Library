from django.contrib import admin


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


class ContributorAdmin(admin.ModelAdmin):
    """Customise list of contributor's names."""
    list_display = ("first_names", "last_names")
    list_filter = ("last_names",)
    search_fields = ("first_names", "last_names__startswith")
