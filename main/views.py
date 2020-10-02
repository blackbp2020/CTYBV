from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import tintuc



# Create your views here.
def index(request): 
    return render(request, 'index.html')


def about(request): 
    return render(request, 'about.html')

def service(request): 
    return render(request, 'service.html')

def news(request):
    queryset = tintuc.objects.all() # list of objects
    context = {
        "object_list": queryset
    }
    #news = tintuc.objects.all() 
    
    return render(request, 'news.html', context)

def newsdetail(request, pk=None):     
    try: 
        p = tintuc.objects.get(pk=pk) 
        context = {
        "object": p
    }
    except tintuc.DoesNotExist: 
        raise Http404("Trang Này Không Tồn Tại Nhé")    
    return render(request, "newsdetail.html", context)
    
    

def lienhe(request): 
    return render(request, 'lienhe.html')