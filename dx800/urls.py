"""dx800 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from dx800_app import views
from django.urls import re_path as url


urlpatterns = [
    path('', views.dept, name='dept'),
    path('admin/', admin.site.urls),
    path('index/', views.index , name='index'),
    path('blank/', views.blank , name='blank'),
    path('defective/', views.defective , name='defective'),
    path('realtime/', views.realtime , name='realtime'),
    path('x_chart/', views.x_chart , name='x_chart'),
    path('spc_chart/', views.spc_chart , name='spc_chart'),
    
]
