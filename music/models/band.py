from django.db import models


class Band(models.Model):
    GENRE = (
        (-1, "not defined"),
        (0, "rock"),
        (1, "metal"),
        (2, "pop"),
        (3, "hip-hop"),
        (4, "electronic"),
        (5, "reggea"),
        (6, "other")
)
    name = models.CharField(max_length=150)
    year = models.IntegerField()
    still_active = models.BooleanField(default=True)
    genre = models.IntegerField(choices = GENRE, default=-1)
    unknown = models.CharField(max_length=10, default="test")