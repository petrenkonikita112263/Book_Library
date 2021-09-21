from django import forms
from .models import Publisher, Review

SEARCH_CHOICES = (
    ("title", "Title"),
    ("contributor", "Contributor")
)


class SearchForm(forms.Form):
    """Searching form that searches for book in database by its title
    or first|last names of contributor."""
    search = forms.CharField(required=False, min_length=3)
    search_in = forms.ChoiceField(required=False, choices=SEARCH_CHOICES)


class PublisherForm(forms.ModelForm):
    """Creates the form based on Publisher model."""

    class Meta:
        model = Publisher
        fields = "__all__"


class ReviewForm(forms.ModelForm):
    """Creates the review form based on Review model, excludes two fields
    and overrides rating field."""

    class Meta:
        model = Review
        exclude = ["date_edited", "book"]

    rating = forms.IntegerField(min_value=0, max_value=5)
