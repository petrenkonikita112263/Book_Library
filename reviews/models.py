from django.db import models
from django.contrib import auth


class Puplisher(models.Model):
    """Represents the table publisher in db, info about a company
    that publishes books."""
    name = models.CharField(
        max_length=50, help_text="The name of the publisher."
    )
    website = models.URLField(
        help_text="The publisher's website link."
    )
    email = models.EmailField(
        help_text="The publisher's contact email address."
    )


class Book(models.Model):
    """Represent the table book in db, info about published book"""
    title = models.CharField(
        max_length=70, help_text="The title of the book."
    )
    publication_date = models.DateField(
        verbose_name="Date the book was published."
    )
    isbn = models.CharField(
        max_length=20, verbose_name="ISBN number of the book."
    )
    publisher = models.ForeignKey(
        Puplisher, on_delete=models.CASCADE
    )


class Contributor(models.Model):
    """A contributor to a book (e.g. author, editor, co-author)."""
    first_names = models.CharField(
        max_length=50, help_text="The contributor's first name or names."
    )
    last_names = models.CharField(
        max_length=50, help_text="The contributor's last name or names."
    )
    email = models.EmailField(
        help_text="The contact email for the contributor."
    )


class Review(models.Model):
    """A information about user-provided review comments and ratings for books."""
    content = models.TextField(
        help_text="The Review text."
    )
    rating = models.IntegerField(
        help_text="The rating the reviewer has given."
    )
    date_created = models.DateTimeField(
        auto_now_add=True, help_text="The date and time the review was created."
    )
    date_edited = models.DateTimeField(
        null=True, help_text="The date and time the review was last edited."
    )
    creator = models.ForeignKey(
        auth.get_user_model(), on_delete=models.CASCADE
    )
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, help_text="The Book that this review is for."
    )
