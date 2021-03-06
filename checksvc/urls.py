"""checksvc URL Configuration

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
from django.urls import path
from django.conf.urls import url
from checksvc.views import HomePageView
from checksvc.views import ServiceListView
from checksvc.views import ServicePageView


urlpatterns = [
    url(r'^service$', ServicePageView.as_view(), name='home'),
    url(r'^$', ServiceListView.as_view(), name='services'),
    url(r'^addsvc$', HomePageView.as_view(), name='service'),

]
