from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
        path('',views.home),
        path('productdetail/<pid>', views.productdetail),
        path('catfilter/<cid>',views.catfilter),
        path('sortbyprice/<s>',views.sortbyprice),
        path('range',views.pricerange),
        path('register/',views.register),
        path('login/',views.user_login),
        path('logout/',views.user_logout),
        path('addtocart/<pid>',views.addtocart),
        path('viewcart/',(views.viewcart)),
        path('remove/<cid>',views.removefromcart),
        path('add_quantity/<cid>/', views.add_quantity),
        path('remove_quantity/<cid>/', views.remove_quantity),
        
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
