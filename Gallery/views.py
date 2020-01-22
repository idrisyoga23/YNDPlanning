from django.shortcuts import render
from .models import GalleryPhoto

# Create your views here.
def Gallery (request):
    #Program = GalleryPhoto.object.all()
    #   response = {'news':news}
    return render(request,'Gallery.html')
def harijadi (request):
    return render(request,'Harijadi.html')
def Gedung (request):
    return render(request,'Gedung.html')