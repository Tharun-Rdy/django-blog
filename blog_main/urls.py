from django.contrib import admin
from django.urls import include, path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('category/', include('blogs.urls')), 
     # any user coming with request category in it, then that request should be forwaded to blogs.urls
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  
