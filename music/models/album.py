from django.db import models

class Album(models.Model):
    # Zpusob hodnoceni
    RATING_CHOICES = [
        (0, "0 stars"),
        (1, "1 star"),
        (2, "2 stars"),
        (3, "3 stars"),
        (4, "4 stars"),
        (5, "5 stars"),
    ]

    album_title = models.CharField(max_length=150)  # nazev alba
    release_year = models.IntegerField()  # rok vydani
    rating = models.IntegerField(choices=RATING_CHOICES, default=0)  # hodnoceni

    def __str__(self):
        return f"{self.album_title} ({self.release_year})"