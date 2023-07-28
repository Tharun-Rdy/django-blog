from django.contrib import admin
from django.urls import include, path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from blogs import views as BlogsView
# As we have already imported views so we take this one as BlogsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('category/', include('blogs.urls')), 
    #Any user coming with request category in it, then that request should be forwaded to blogs.urls
    path('<slug:slug>/', BlogsView.blogs, name='blogs'),
    # search endpoint
    path('blogs/search', BlogsView.search, name='search'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  
