from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from apps.training.models import Student,Teacher,Course,Score
from apps.training.api.serializers import StudentSerializer,TeacherSerializer,CourseSerializer,ScoreSerializer

#---------Student API-----------------
#------------------------------------
@api_view(['GET','POST'])
def student_api_view(request):

    if request.method == 'GET':
        student=Student.objects.all()
        students_serializer = StudentSerializer(student,many=True)
        return Response (students_serializer.data,status=status.HTTP_200_OK)
    
    elif request.method =='POST':
        student_serializer = StudentSerializer(data= request.data)

        if student_serializer.is_valid():
            student_serializer.save()
            return Response(student_serializer.data,status=status.HTTP_201_CREATED)
        return  Response(student_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET','PUT','DELETE'])
def student_detail_api_view(request,docu=None):

    student=Student.objects.filter(document=docu).first()

    if student:

        if request.method == 'GET':

            student_serializer = StudentSerializer(student)
            return Response(student_serializer.data, status=status.HTTP_200_OK)
        
        elif request.method == 'PUT':

            student_serializer = StudentSerializer(student,data=request.data)

            if student_serializer.is_valid():
                student_serializer.save()
                return Response (student_serializer.data,status=status.HTTP_400_BAD_REQUEST)
            return Response(student_serializer.errors)
        
        elif request.method == 'DELETE':

            student.delete()
            return Response ({'message':'student successfully removed'},status=status.HTTP_200_OK)
    
    return Response({'mesage':'No student found with these data'},status=status.HTTP_400_BAD_REQUEST)

#------------ Teacher API-----------------------
#-----------------------------------------------
@api_view(['GET','POST'])
def teacher_api_view(request):

    if request.method == 'GET':
        teacher=Teacher.objects.all()
        teacher_serializer = StudentSerializer(teacher,many=True)
        return Response (teacher_serializer.data,status=status.HTTP_200_OK)
    
    elif request.method =='POST':
        teacher_serializer = TeacherSerializer(data= request.data)

        if teacher_serializer.is_valid():
            teacher_serializer.save()
            return Response(teacher_serializer.data,status=status.HTTP_201_CREATED)
        return  Response(teacher_serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def teacher_detail_api_view(request,docu=None):

    teacher = Teacher.objects.filter(document=docu).first()

    if teacher:

        if request.method == 'GET':

            teacher_serializer = TeacherSerializer(teacher)
            return Response(teacher_serializer.data, status=status.HTTP_200_OK)
        
        elif request.method == 'PUT':

            teacher_serializer=TeacherSerializer(teacher,data=request.data)

            if teacher_serializer.is_valid():
                teacher_serializer.save()
                return Response (teacher_serializer.data,status=status.HTTP_400_BAD_REQUEST)
            return Response(teacher_serializer.errors)
        
        elif request.method == 'DELETE':

            teacher.delete()
            return Response ({'message':'Teacher successfully removed'},status=status.HTTP_200_OK)
    
    return Response({'mesage':'No Teacher found with these data'},status=status.HTTP_400_BAD_REQUEST)


#---------Course API-----------------
#------------------------------------
@api_view(['GET','POST'])
def course_api_view(request):

    if request.method == 'GET':
        course=Course.objects.all()
        course_serializer = CourseSerializer(course,many=True)
        return Response (course_serializer.data,status=status.HTTP_200_OK)
    
    elif request.method =='POST':
        course_serializer = CourseSerializer(data= request.data)

        if course_serializer.is_valid():
            course_serializer.save()
            return Response(course_serializer.data,status=status.HTTP_201_CREATED)
        return  Response(course_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','PUT','DELETE'])
def course_detail_api_view(request,name_course=None):

    course = Course.objects.filter(name=name_course).first()

    if course:

        if request.method == 'GET':

            course_serializer=CourseSerializer(course)
            return Response(course_serializer.data, status=status.HTTP_200_OK)
        
        elif request.method == 'PUT':

            course_serializer=CourseSerializer(course,data=request.data)

            if course_serializer.is_valid():
                course_serializer.save()
                return Response (course_serializer.data,status=status.HTTP_400_BAD_REQUEST)
            return Response(course_serializer.errors)
        
        elif request.method == 'DELETE':

            course.delete()
            return Response ({'message':'Course successfully removed'},status=status.HTTP_200_OK)
    
    return Response({'mesage':'No Course found with these data'},status=status.HTTP_400_BAD_REQUEST)


#---------Score API-----------------
#-----------------------------------
@api_view(['GET','POST'])
def score_api_view(request):

    if request.method == 'GET':
        score=Score.objects.all()
        scoreSerializer = ScoreSerializer(score,many=True)
        return Response (scoreSerializer.data,status=status.HTTP_200_OK)
    
    elif request.method =='POST':
        scoreSerializer = ScoreSerializer(data= request.data)

        if scoreSerializer.is_valid():
            scoreSerializer.save()
            return Response(scoreSerializer.data,status=status.HTTP_201_CREATED)
        return  Response(scoreSerializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET','PUT','DELETE'])
def score_detail_api_view(request,docu=None,name_course=None):

    
    student = Student.objects.filter(document=docu).first()
    course = Course.objects.filter(name=name_course).first()
    
    if student and course:

        score = Score.objects.filter(student_id=student,course_id=course).first()

        if score:

            if request.method == 'GET':

                scoreSerializer=ScoreSerializer(score)
                return Response(scoreSerializer.data, status=status.HTTP_200_OK)
            
            elif request.method == 'PUT':

                scoreSerializer = ScoreSerializer(score,data=request.data)

                if scoreSerializer.is_valid():
                    scoreSerializer.save()
                    return Response (scoreSerializer.data,status=status.HTTP_400_BAD_REQUEST)
                return Response(scoreSerializer.errors)
            
            elif request.method == 'DELETE':

                score.delete()
                return Response ({'message':'Score successfully removed'},status=status.HTTP_200_OK)
            
        return Response({'mesage':'The student does not have scores in the system'},status=status.HTTP_400_BAD_REQUEST)
    
    return Response({'mesage':'No Scores found with these data'},status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def score_by_student_api_view(request,docu=None):

    
    student = Student.objects.filter(document=docu).first()
    
    if student:

        score = Score.objects.filter(student_id=student)

        if score:

            if request.method == 'GET':

                scoreSerializer = ScoreSerializer(score,many=True)
                return Response(scoreSerializer.data, status=status.HTTP_200_OK)
            
            
            
        return Response({'mesage':'The student does not have scores in the system'},status=status.HTTP_400_BAD_REQUEST)
    
    return Response({'mesage':'No Scores found with these data, student do not exits'},status=status.HTTP_400_BAD_REQUEST)