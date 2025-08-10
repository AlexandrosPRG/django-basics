from django.db import models


class Car(models.Model):
    COLORS = (
        (1, "red"),
        (2, "blue"),
        (3, "white"),
        (4, "black")
)
    color = models.IntegerField(choices = COLORS)