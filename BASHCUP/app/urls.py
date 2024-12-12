from django.contrib import admin
from django.urls import path
from .import views
from django.conf.urls.static import static
from django.conf import settings

from django.views.static import serve
from django.conf.urls import url

urlpatterns = [
    path('', views.home),
    path('menu', views.menu),
    path('handicraft', views.handicraft),
    path('feedback', views.feedback),
    url(r'^media/(?p<path>.*)$',serve,{'document_root':  settings. MEDIA_ROOT}),
    url(r'^static/(?p<path>.*)$',serve,{'document_root':  settings. STATIC_ROOT}),
    
]

urlpatterns+= static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
