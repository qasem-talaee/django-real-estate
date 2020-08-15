"""real_estate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('blog/', blog, name="blog"),
    path('blog/page/<int:page>/', blog_page, name='blog_page'),
    path('blog-detail/<slug:url>/', blog_detail, name="blog_detail"),
    path('property/', property, name="property"),
    path('property/page/<int:page>/', property_page, name="property_page"),
    path('property-detail/<int:id>/', property_detail, name="property_detail"),
    path('contact/', contact, name="contact"),
    path('agent/', agent, name="agent"),
    ###########SEARCH
    path('search/', search, name="search"),
    path('agent-contact/agent/<int:id>/property/<int:prop_id>/', agent_contact, name="agent_contact"),
    ###########CKEDITOR URLS
    path('^ckeditor/', include('ckeditor_uploader.urls')),
]

admin.site.site_header = "Real Estate Admin"
admin.site.site_title = "Real Estate Portal"
admin.site.index_title = "Welcome to Real Estate Portal"

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)