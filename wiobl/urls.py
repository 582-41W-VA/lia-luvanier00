"""
URL configuration for wiobl project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from wioblapp.admin import wiobl_site

urlpatterns = [
    path("wioblapp/", include("wioblapp.urls")),
    path("admin/", wiobl_site.urls),
]

wiobl_site.index_title = "West Island Outdoor Basketball League"
wiobl_site.site_header = "W.I.O.B.L Admin"
wiobl_site.site_title = "W.I.O.B.L"
