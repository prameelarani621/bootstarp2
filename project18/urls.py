"""
URL configuration for project18 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from app.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('bootstarp_downlods/',bootstarp_downlods,name='bootstarp_downlods'),
    path('alerts/',alerts,name='alerts'),
    path('new/',new,name='new'),
    path('one/',one,name='one'),
    path('alerts2/',alerts2,name='alerts2'),
    path('notification/',notification,name='notification'),
    path('keys/',keys,name='keys'),
    path('home/',home,name='home'),
    path('button/',button,name='button'),
    path('b1/',b1,name='b1'),
    path('b2/',b2,name='b2'),
    path('b3/',b3,name='b3'),
    path('b4/',b4,name='b4'),
    path('b5/',b5,name='b5'),
    path('b6/',b6,name='b6'),
    path('b7/',b7,name='b7'),
    path('b8/',b8,name='b8'),
    path('b9/',b9,name='b9'),
    path('b10/',b10,name='b10'),
    path('b11/',b11,name='b11'),
    path('b12/',b12,name='b12'),
    path('b13/',b13,name='b13'),
    path('b14/',b14,name='b14'),
]
