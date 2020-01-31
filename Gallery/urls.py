from django.urls import path
from . import views

urlpatterns = [
    path('',views.Gallery,name = 'Gallery'),
    path('harijadi/',views.harijadi,name = 'harijadi'),
    path('Gedung/',views.Gedung,name = 'Gedung'),
    path('Venue/',views.Venue,name = 'Venue')
]
