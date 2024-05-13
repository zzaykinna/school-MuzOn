"""
URL configuration for Muz_On project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from myapp1.views import teacher_page,about_page, index_page, timing_page,profession_page, write_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_page),
    path('about/', about_page),
    path('timing/', timing_page),
    path('teacher/', teacher_page),
    path('profession/', profession_page),
    path('write/', write_page),
]
