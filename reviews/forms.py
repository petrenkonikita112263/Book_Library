from django import forms


class SearchForm(forms.Form):
    """Searching form that searches for book in database by its title
    or first|last names of contributor."""
    pass
