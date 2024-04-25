from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlspattern = [
        path('',(views.index)),
]

if settings.DEBUG:
    urlspattern += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
