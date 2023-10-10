from django.db import models
from django.contrib.auth.models import User

class Berita(models.Model):
    judul = models.CharField(max_length=200)
    gambar = models.ImageField(null=False, blank=False, upload_to='image')
    konten = models.TextField()
    penulis = models.ForeignKey(User, on_delete=models.CASCADE)
    tanggal_publikasi = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.judul