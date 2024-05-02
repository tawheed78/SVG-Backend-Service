from django.db import models


class Game(models.Model):
    """A model to represent a game."""
    name = models.CharField(max_length=50)
    url = models.URLField(max_length=200, unique=True)
    author = models.CharField(max_length=50)
    published_date = models.DateField()
