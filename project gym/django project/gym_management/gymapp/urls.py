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
    path('personal-training/', views.personaltraining, name='personaltraining'),
    path('classes/', views.classes, name='classes'),
    path('workout/kickboxing/', views.kickboxing, name='kickboxing'),
    path('workout/indoor-cycling/', views.indoorcycling, name='indoorcycling'),
    path('workout/zumba-fitness/', views.zumbafitness, name='zumbafitness'),
    path('workout/power-yoga/', views.poweryoga, name='poweryoga'),
    path('body-composition-assessment/', views.nutrition, name='nutrition'),
    path('careers/', views.careers, name='careers'),
    path('location/', views.location, name='location'),
    path('about-us/', views.aboutus, name='aboutus'),
]

# if settings.DEBUG:  
#     urlspattern += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)