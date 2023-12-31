"""
URL configuration for scoreslsv project.

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
from django.urls import path,include
from apps.training.views import Home,Processing

urlpatterns = [
    path('admin/', admin.site.urls),
    path('training/',include(('apps.training.urls','training'))),
    path('home/',Home,name='index'),
    path('processing/',Processing,name='processing'),
    path('student/',include('apps.training.api.urls')),
    path('teacher/',include('apps.training.api.urls')),
    path('course/',include('apps.training.api.urls')),
    path('score/',include('apps.training.api.urls'))
    
    
]
