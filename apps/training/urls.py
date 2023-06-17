from django.urls import path
from .views import uploaderInfo

urlpatterns = [
    path('load_info/',uploaderInfo,name='load_info'),
   
    
]