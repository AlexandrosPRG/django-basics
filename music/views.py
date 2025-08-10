from django.shortcuts import render, get_object_or_404, redirect
from .models import Band
from .models import Album, Song

def band_list(request):
    bands = Band.objects.all()
    return render(request, "band_list.html", {"bands": bands})

def band_detail(request, band_id):
    band = get_object_or_404(Band, id=band_id)
    return render(request, "band_detail.html", {"band": band})

def album_list(request):
    albums = Album.objects.all().order_by("-release_year")
    return render(request, "album_list.html", {"albums": albums})

# Vytvoření nového alba (GET: formulář, POST: uložení)
def album_create(request):
    if request.method == "POST":
        # načtení hodnot z formuláře
        title = request.POST.get("album_title")
        year = request.POST.get("release_year")
        rating = request.POST.get("rating", 0)

        # jednoduchá validace (minimální)
        if not title or not year:
            return render(request, "album_create.html", {
                "error": "Vyplň název a rok.",
            })

        # vytvoření alba
        a = Album.objects.create(
            album_title=title,
            release_year=int(year),
            rating=int(rating),
        )
        # po vytvoření jdeme rovnou na detail
        return redirect("album_detail", album_id=a.id)

    # GET – zobraz formulář
    return render(request, "album_create.html")

# Detail alba + seznam songů
def album_detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    # jen zobrazení; samotné přidání songu řešíme ve song_add
    return render(request, "album_detail.html", {"album": album})

# Přidání songu do konkrétního alba (přes POST)
def song_add(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    if request.method != "POST":
        return redirect("album_detail", album_id=album.id)

    # načteme data z formuláře
    title = request.POST.get("title")
    duration = request.POST.get("duration")  # očekává "HH:MM" nebo prázdné

    if not title:
        return render(request, "album_detail.html", {
            "album": album,
            "error": "Zadej název skladby."
        })

    # vytvoříme song; duration může být None/"" – TimeField snese null když je null=True
    # pokud máš v modelu TimeField(null=True, blank=True), prázdné pole je OK
    Song.objects.create(
        title=title,
        duration=duration if duration else None,
        album=album,
    )
    return redirect("album_detail", album_id=album.id)

def band_create(request):
    if request.method == "POST":
        name = request.POST["name"]
        year = request.POST["year"]
        genre = request.POST["genre"]
        Band.objects.create(name=name, year=year, genre=genre)
        return redirect("band_list")
    # ⚠️ render BEZ prefixu "music/"
    return render(request, "band_create.html", {"genres": Band.GENRE})