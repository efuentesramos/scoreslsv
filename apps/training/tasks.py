
import pandas as pd
from .models import Student,Teacher,Course,Score
from apps.training.utils.validator import ValidatorField

from celery import Celery
from celery.signals import task_success

app = Celery('tasks', broker='pyamqp://guest@localhost//')


@app.task
def loadStudent(file_data):
    
    colunm_required={'nombre','apellido','documento','edad','email','genero','direccion','hoobies'}
    try:
       
        df_student=pd.read_excel(file_data,"ESTUDIANTE")
        colunm_names_df=set(df_student.columns.values)
        print(colunm_names_df)
       
        if isinstance( df_student,pd.core.frame.DataFrame) and colunm_required.issubset(colunm_names_df):
            
            for index,row in df_student.iterrows():

                try:
                    obj = Student.objects.get(document__exact=row['documento'])
                except Student.DoesNotExist:
                    
                    if (
                        (ValidatorField.isPositiveNumber(row['edad'])) and 
                        (ValidatorField.isFormatEmail(row['email'])) and 
                        (ValidatorField.isPositiveNumber(row['documento']))and
                        (ValidatorField.isValidGender(row['genero']))
                        
                        ):
                        obj = Student(name=row['nombre'], 
                                    last_name=row['apellido'],
                                    address=row['direccion'],
                                    email=row['email'],
                                    document=row['documento'],
                                    gender=row['genero'], 
                                    age=row['edad'],
                                    hobbies=row['hoobies'],
                                )
                        obj.save()
                    else:
                        print(f"registro {index} presento datos no validos en la hoja Estudiante")
            
            
        else:
             print("NO SE PUEDE COMPROBAR EL DF")
        
    except Exception as error_plan:
        pass    

@task_success.connect(sender=loadStudent)
def loadTeacher(sender=None, args=None, file_data=None, **kwargs):
    
    colunm_required={'nombre','apellido','documento','edad','email','genero','direccion','salario'}
    try:
            
        df_teacher = pd.read_excel(file_data,"PROFESOR")
        colunm_names_df=set(df_teacher.columns.values)
        if isinstance( df_teacher,pd.core.frame.DataFrame) and colunm_required.issubset(colunm_names_df):
            print("#####--EL DF TEACHER fue generado con EXITO-#####")
            print("#----buscando ")

            for index,row in df_teacher.iterrows():

                try:
                    obj = Teacher.objects.get(document__exact=row['documento'])
                except Teacher.DoesNotExist:

                    if (
                        (ValidatorField.isPositiveNumber(row['edad'])) and 
                        (ValidatorField.isFormatEmail(row['email'])) and 
                        (ValidatorField.isPositiveNumber(row['documento']))and
                        (ValidatorField.isValidGender(row['genero']))and
                        (ValidatorField.isPositiveNumber(row['salario']))
                        
                        ):

                        obj = Teacher(name=row['nombre'], 
                                    last_name=row['apellido'],
                                    address=row['direccion'],
                                    email=row['email'],
                                    document=row['documento'],
                                    gender=row['genero'], 
                                    age=row['edad'],
                                    salary=row['salario'],
                                )
                        obj.save()
        else:
             print("NO SE PUEDE COMPROBAR EL DF")


    except Exception as error_plan:
        pass
    

task_success.connect(sender=loadTeacher)
def loadCourse(sender=None, args=None, file_data=None, **kwargs):

    colunm_required={'nombre','descripcion','horas','documentoProfesor'}
    
    try:    
        df_course = pd.read_excel(file_data,"CURSO")
        colunm_names_df=set(df_course.columns.values)
        if isinstance( df_course,pd.core.frame.DataFrame) and colunm_required.issubset(colunm_names_df):

            for index,row in df_course.iterrows():

                try:
                    obj = Course.objects.get(name__iexact=row['nombre'])
                except Course.DoesNotExist:

                    try:
                        teacher=Teacher.objects.get(document__exact=row['documentoProfesor'])
                        if teacher and (ValidatorField.isPositiveNumber(row['horas'])):
                            obj = Course(name=row['nombre'], 
                                description=row['descripcion'],
                                total_hours=row['horas'],
                                teacher_id=teacher,
                            )
                            obj.save()

                    except Teacher.DoesNotExist:

                        print("registro a novedades de importacion")
            
    except Exception as error_plan:
        pass 
    

task_success.connect(sender=loadCourse)
def loadScores(sender=None, args=None, file_data=None, **kwargs):

    colunm_required={'calificacion','curso','documentoEstudiante'} 
    try:
        df_scores = pd.read_excel(file_data,"CALIFICACIONES")
        colunm_names_df=set(df_scores.columns.values)

        if isinstance( df_scores,pd.core.frame.DataFrame) and colunm_required.issubset(colunm_names_df):
            
            #ValidatorField.RangeScores(row['calificacion'])
            for index,row in df_scores.iterrows():       
                try:
                    student_obj = Student.objects.get(document__exact=row['documentoEstudiante'])
                    course_obj = Course.objects.get(name__iexact=row['curso'])
                    print(ValidatorField.RangeScores(row['calificacion']))
                    if (student_obj and course_obj and ValidatorField.RangeScores(row['calificacion'])):
                        obj = Score(course_id=course_obj, 
                                student_id=student_obj,
                                final_score=row['calificacion'],
                                )
                        obj.save()
                    else:
                        print('no existe estudiantes y profesores con los datos del registro')
                        
                except Exception:
                    
                    print("registro a novedades de importacion")
        
    except Exception as error_plan:
        pass 

    
