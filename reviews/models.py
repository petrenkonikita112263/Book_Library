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
