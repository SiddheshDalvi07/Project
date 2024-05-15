from django.conf import settings
from django.urls import path
from . import views
from django.conf.urls import static

urlpatterns = [
    path('', views.index, name='index'),
    path('offers/', views.offers, name='offers'),
    path('offers/1-day-free-guest-pass/', views.freepass, name='1-day-free-guest-pass'),
]

# if settings.DEBUG:  
#     urlspattern += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)