from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Publisher, Review, Book

SEARCH_CHOICES = (
    ("title", "Title"),
    ("contributor", "Contributor")
)


class SearchForm(forms.Form):
    """Searching form that searches for book in database by its title
    or first|last names of contributor."""
    search = forms.CharField(required=False, min_length=3)
    search_in = forms.ChoiceField(required=False, choices=SEARCH_CHOICES)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "get"
        self.helper.add_input(Submit("", "Search"))



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


class BookMediaForm(forms.ModelForm):
    """Creates the form for uploading cover and sample of the book."""

    class Meta:
        model = Book
        fields = ["cover", "sample"]
