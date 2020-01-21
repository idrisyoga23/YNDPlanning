from django.shortcuts import render
from .models import GalleryPhoto

# Create your views here.
def Gallery (request):
    #Program = GalleryPhoto.object.all()
    #   response = {'news':news}
    return render(request,'Gallery.html')