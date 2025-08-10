from django.contrib import admin
from .models import Article
from .models import Album

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ("album_title", "release_year", "rating")
    list_filter = ("rating", "release_year")
    search_fields = ("album_title",)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "status", "publish_date", "date_added")
    list_filter = ("status", "publish_date", "removal_date", "date_added")
    search_fields = ("title", "author", "content")
