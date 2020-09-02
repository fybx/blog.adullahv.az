from django.shortcuts import render,HttpResponse,get_object_or_404,HttpResponseRedirect,redirect
from .models import post
from .forms import postform
from django.contrib import messages
from django.db.models import Q
# Create your views here.


def home(request):
    context = {
        'isim':'Abdullah',
        'soyisim':'Veliyev'
    }
    return render(request,'home.html',context)

def postlar(request):
    tumpostlar1 = post.objects.all()
    query = request.GET.get("sorgu")
    if query:
        tumpostlar1 = tumpostlar1.filter(
            Q(baslik__icontains = query)|
            Q(metin__icontains = query)|
            Q(kategori__icontains = query)|
            Q(aciklama__icontains = query)
            )
    sayi = len(tumpostlar1)
    context = {
        'tumpostlar1':tumpostlar1,
        'sayi':sayi,
        'query':query
        }
    
    return render(request,'postlar.html',context)

def detallar(request,id):
    tumpostlar2 = get_object_or_404(post,id=id)
    return render(request,'detallar.html',{'tumpostlar2':tumpostlar2})

def duzenle(request,id):
    tumpostlar2 = get_object_or_404(post,id=id)
    form = postform(request.POST or None,instance=tumpostlar2)
    if form.is_valid():
        save = form.save()
        messages.success(request,'Postunuz Basariyla degistirildi!')
        return HttpResponseRedirect(save.get_absolute_url())
    context = {
        'form':form,
    }
    return render(request,'forms.html',context)

def bos(request):
    return render(request,'bos.html',{})
    
def forms(request):
    #form = postform(request.POST or None)

    if request.method == "POST":
        form = postform(request.POST)
        if form.is_valid():
            save = form.save()
            messages.success(request,'postunuz olusturuldu!')
            return HttpResponseRedirect(save.get_absolute_url())
    else:
        form = postform()
    context = {
        'form':form,
    }
    return render(request,'forms.html',context)



def sil(request,id):
    postsil = get_object_or_404(post,id=id)
    postsil.delete()
    messages.success(request,'postunuz silindi!')
    return redirect('postlar')
    

def hakkimda(request):
    return render(request, 'hakkimda.html',{})


def iletisim(request):
    return render(request, 'iletisim.html',{})
    

def kategoriya(request,kategori):
    kategorilipost = post.objects.filter(kategori=kategori)
    katsayi = len(kategorilipost)
    context = {
        'kategorilipost':kategorilipost,
        'katsayi':katsayi
    }
    return render(request,"kategori.html",context)