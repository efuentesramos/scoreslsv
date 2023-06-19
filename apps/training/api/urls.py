from django.urls import path
from apps.training.api.api import student_api_view, student_detail_api_view,\
teacher_api_view,teacher_detail_api_view,course_api_view,course_detail_api_view,\
score_api_view,score_detail_api_view,score_by_student_api_view


urlpatterns =[
    path('student/',student_api_view, name='student_api'),
    path('student/<int:docu>/',student_detail_api_view, name='student_detail_api_view'),
    path('teacher/',teacher_api_view, name='teacher_api'),
    path('teacher/<int:docu>/',teacher_detail_api_view, name='teacher_detail_api_view'),
    path('course/',course_api_view, name='course_api'),
    path('course/<str:name_course>/',course_detail_api_view, name='course_detail_api_view'),
    path('score/',score_api_view, name='score_api'),
    path('score/<int:docu>/<str:name_course>/',score_detail_api_view, name='score_detail_api_view'),
    path('scores_student/<int:docu>/',score_by_student_api_view, name='score_by_student_api_view'),
]