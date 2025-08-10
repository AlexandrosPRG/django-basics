from django.urls import path
from . import views

urlpatterns = [
    path("bands/", views.band_list, name="band_list"),
    path("bands/<int:band_id>/", views.band_detail, name="band_detail"),
    path("bands/create/", views.band_create, name="band_create"),
    path("albums/", views.album_list, name="album_list"),  # seznam alb
    path("albums/create/", views.album_create, name="album_create"),  # vytvoření alba
    path("albums/<int:album_id>/", views.album_detail, name="album_detail"),  # detail + přidání songu
    path("albums/<int:album_id>/add-song/", views.song_add, name="song_add"),  # endpoint pro přidání songu
]