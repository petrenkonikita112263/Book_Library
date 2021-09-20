from django import forms
from .models import Publisher

SEARCH_CHOICES = (
    ("title", "Title"),
    ("contributor", "Contributor")
)


class SearchForm(forms.Form):
    """Searching form that searches for book in database by its title
    or first|last names of contributor."""
    search = forms.CharField(required=False, min_length=3)
    search_in = forms.ChoiceField(required=False, choices=SEARCH_CHOICES)
