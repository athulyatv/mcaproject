"""sample URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
from app1 import views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('page1/',views.home),
    path('about/',views.aboutf),
    path('contact/',views.contactf),
    path('login/',views.loginf),
    path('student/',views.studentf),
    path('reg/',views.regf),
    path('index/',views.indexf),
    path('gallery/',views.galleryf),
    path('about1/',views.about1f),
    path('insert/',views.insert),
    path('dept/',views.deptf),
    path('insertion/',views.insertionf),
    path('viewdata1/',views.viewdata1f),
    path('removedept/<str:id1>',views.removedeptf),

   
]
