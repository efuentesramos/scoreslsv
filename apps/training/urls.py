from django.urls import path
from .views import uploaderInfo,loadCourseFramPage

urlpatterns = [
    path('load_info/',uploaderInfo,name='load_info'),
    path('courses_load/',loadCourseFramPage,name='load_course'),
   
    
]