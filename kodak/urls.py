from django.urls import path

from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('main/', views.main, name='main'),
    path('blueprints/', views.blueprints, name='blueprints'),
    path('brochure_printing/', views.brochure_printing, name='brochure_printing'),
    path('document_printing/', views.document_printing, name='document_printing'),
    path('order/', views.order, name='order'),
    path('photo_printing/', views.photo_printing, name='photo_printing'),
    path('photo_processing/', views.photo_processing, name='photo_processing'),
    path('services/', views.services, name='services'),
    path('shirt_printing/', views.shirt_printing, name='shirt_printing')
]