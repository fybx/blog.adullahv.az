from django.db import models
from django.utils import timezone
from django.urls import reverse
from ckeditor.fields import RichTextField



simdi = timezone.now()
class post(models.Model):
    baslik = models.CharField(max_length=40)
    kategori = models.CharField(max_length=30,default="Kateqoriyasiz")
    metin = RichTextField()
    aciklama = models.TextField()
    tarih = models.DateTimeField(default = simdi)
    resim = models.FileField(blank=True,null=True)
    

    def __str__(self):
        return self.baslik

    def get_absolute_url(self):
        return reverse('detallar',kwargs={'id':self.id})
        #return "post/duzenle/{}".format(self.id)

    class Meta:
        ordering=['-id']


