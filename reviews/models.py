from django.db import models
from django.contrib import auth


class Publisher(models.Model):
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

    def __str__(self):
        """Prints the publisher name."""
        return self.name


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
        Publisher, on_delete=models.CASCADE
    )
    contributors = models.ManyToManyField(
        "Contributor", through="BookContributor"
    )

    def __str__(self):
        """Prints the book name."""
        return self.title


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

    def initialled_name(self):
        """Create string with first name as initials and second name."""
        initials = "".join(
            [name[0] for name in self.first_names.split(" ")]
        )
        return f"{self.last_names}, {initials}"

    def __str__(self):
        """Prints the contributor name(s)."""
        return self.initialled_name()


class BookContributor(models.Model):
    """A info about book and contributor's type."""

    class ContributionRole(models.TextChoices):
        """A set of choices for contribution type."""
        AUTHOR = "AUTHOR", "Author"
        CO_AUTHOR = "CO_AUTHOR", "Co-Author"
        EDITOR = "EDITOR", "Editor"

    book = models.ForeignKey(
        Book, on_delete=models.CASCADE
    )
    contributor = models.ForeignKey(
        Contributor, on_delete=models.CASCADE
    )
    role = models.CharField(
        verbose_name="The role this contributor had in the book.", choices=ContributionRole.choices,
        max_length=20
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

    def __str__(self):
        """Prints the review content for a book."""
        return self.content
