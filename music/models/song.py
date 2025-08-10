from django.db import models
from .album import Album  # import stávajícího modelu Album

class Song(models.Model):
    # Název skladby (max 128 znaků)
    title = models.CharField(max_length=128)

    # Doba trvání – podle zadání TimeField; může být prázdné
    duration = models.TimeField(null=True, blank=True)

    # Vazba N:1 – jeden album má mnoho skladeb
    album = models.ForeignKey(
        Album,
        on_delete=models.CASCADE,   # při smazání alba smažeme i jeho skladby
        related_name="songs"        # umožní album.songs.all()
    )

    def __str__(self):
        # hezké zobrazení v adminu
        return f"{self.title} – {self.album}"
