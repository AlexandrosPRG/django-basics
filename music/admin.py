from django.contrib import admin
from .models import Album, Song

class SongInline(admin.TabularInline):
    model = Song
    extra = 1  # cz: kolik prázdných řádků pro rychlé přidání

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ("album_title", "release_year", "rating")
    inlines = [SongInline]

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ("title", "album", "duration")
    list_filter = ("album",)
    search_fields = ("title",)
