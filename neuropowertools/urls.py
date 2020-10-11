"""neuropowertools URL Configuration

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
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles import views
from django.urls import re_path
from .apps.main.views import home
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .apps import power

urlpatterns = [
    path('', home, name = 'home'),
    path('power/', include(power.urls))
    # path('neuropower', include(neuropowertoolbox.urls))
]
