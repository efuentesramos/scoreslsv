from django.contrib import admin
from .models import Student,Teacher,Course,Score
# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    pass

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass

@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
    pass