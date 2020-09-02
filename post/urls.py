from django.conf.urls import url,include
from .views import home,postlar,duzenle,detallar,forms,sil,hakkimda,iletisim
urlpatterns = [
    url(r'^$',home),
    url(r'^postlar$',postlar,name='postlar'),
    url(r'^postlar/detallar/(?P<id>\d+)/$',detallar,name='detallar'),
    url(r'^duzenle/(?P<id>\d+)/$',duzenle),
    url(r'^forms$',forms),
    url(r'^sil/(?P<id>\d+)/$',sil),
    url(r'^hakkimda$', hakkimda),
    url(r'^iletisim$', iletisim)
]


