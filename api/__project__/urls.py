"""Project's root URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
https://docs.djangoproject.com/en/dev/topics/http/urls/
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.views.debug import default_urlconf

urlpatterns = [
    path('', default_urlconf),
    path('admin/', admin.site.urls),
]

if settings.ENVIRONMENT == 'DEVELOPMENT':
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
