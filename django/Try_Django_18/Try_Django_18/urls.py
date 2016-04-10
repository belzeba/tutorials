"""Try_Django_18 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static

# Different views (own)
from newsletter import views as newsletter_views
from contact import views as contact_views
from Try_Django_18 import views as trydjango_views

urlpatterns = [
    # URL for homepage
    url(r'^$', newsletter_views.home, name='home'),
    # URL for contact page
    url(r'^contact/$', contact_views.contact, name='contact'),
    # URL for about page
    url(r'^about/$', trydjango_views.about, name='about'),
    # URL for admin page
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
