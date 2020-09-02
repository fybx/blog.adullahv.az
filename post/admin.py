from django.contrib import admin

from .models import post

# Register your models here.

class filtre(admin.ModelAdmin):
    list_display = ['baslik','tarih']
    list_filter = ['kategori','tarih']
    search_fields = ['baslik','metin']
    list_display_links = ['tarih','baslik']

    class Meta:
        model = post


admin.site.register(post,filtre)
