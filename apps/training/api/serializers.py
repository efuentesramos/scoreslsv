from rest_framework import serializers
from apps.training.models import Student,Teacher,Course,Score


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = '__all__'

class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'


class ScoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Score
        fields = '__all__'
