from django.shortcuts import render
from .models import Berita

def daftar_berita(request):
    berita = Berita.objects.all()
    return render(request, 'berita/index.html', {'berita': berita})

def detail_berita(request, id):
    berita = Berita.objects.get(id=id)
    print(berita)
    return render(request, 'berita/detail_berita.html', {'berita': berita})
