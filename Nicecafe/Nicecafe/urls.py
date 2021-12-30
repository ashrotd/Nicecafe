 
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls import url

from django.views.static import serve
from django.conf import settings
from Nicecafe.settings import MEDIA_ROOT
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('book/', include('book.urls')),
    path('contact/', include('contact.urls')),
    path('our_story/', views.about, name='about'),
    path('career/', include('career.urls')),
    path('menu/',include('menu.urls')),
      url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
] + static(settings.MEDIA_URL, document_root = MEDIA_ROOT)
