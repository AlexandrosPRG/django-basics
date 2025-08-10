from django.shortcuts import render, get_object_or_404, redirect
from .models import Band

def band_list(request):
    bands = Band.objects.all()
    return render(request, "band_list.html", {"bands": bands})

def band_detail(request, band_id):
    band = get_object_or_404(Band, id=band_id)
    return render(request, "band_detail.html", {"band": band})

def band_create(request):
    if request.method == "POST":
        name = request.POST["name"]
        year = request.POST["year"]
        genre = request.POST["genre"]
        Band.objects.create(name=name, year=year, genre=genre)
        return redirect("band_list")
    # ⚠️ render BEZ prefixu "music/"
    return render(request, "band_create.html", {"genres": Band.GENRE})