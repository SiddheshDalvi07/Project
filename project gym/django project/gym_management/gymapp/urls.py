from django.conf import settings
from django.urls import path
from . import views
from django.conf.urls import static

urlpatterns = [
    path('', views.index, name='index'),
]

# if settings.DEBUG:  
#     urlspattern += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)