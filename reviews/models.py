from django.db import models

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
    
