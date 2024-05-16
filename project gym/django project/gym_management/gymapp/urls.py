from django.conf import settings
from django.urls import path
from . import views
from django.conf.urls import static

urlpatterns = [
    path('', views.index, name='index'),
    path('offers/', views.offers, name='offers'),
    path('offers/1-day-free-guest-pass/', views.freepass, name='1-day-free-guest-pass'),
    path('offers/accelerate-recovery-with-normatec-air-compression/', views.accrecovery, name='accelerate-recovery-with-normatec-air-compression'),
    path('offers/abcoffee/', views.abcoffee, name='abcoffee'),
    path('offers/start-today-at-waves-gym-safesweatspace/', views.starttoday, name='starttoday'),
    path('offers/rapid-muscle-relief/', views.rapidmuscle, name='rapidmuscle'),
    path('offers/refer-a-friend/', views.referafriend, name='referafriend'),
    path('membership/', views.membership, name='membership'),
]

# if settings.DEBUG:  
#     urlspattern += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)