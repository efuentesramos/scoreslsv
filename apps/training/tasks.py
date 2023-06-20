
import pandas as pd
import requests, bs4
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from .models import Student,Teacher,Course,Score
from apps.training.utils.validator import ValidatorField

from celery import Celery
from celery.signals import task_success

app = Celery('tasks', broker='pyamqp://guest@localhost//')

status_load={'load_student':{'successful_lines':0,
                         'lines_with_errors':0,
                         'existing_record':0,},
                'load_teacher':{'successful_lines':0,
                         'lines_with_errors':0,
                         'existing_record':0},
                'load_course':{'successful_lines':0,
                         'lines_with_errors':0,
                         'existing_record':0},
                'load_scores':{'successful_lines':0,
                         'lines_with_errors':0,
                         'existing_record':0}
                }

@app.task
def loadStudent(file_data):
    
    colunm_required={'nombre','apellido','documento','edad','email','genero','direccion','hoobies'}
    try:
       
        df_student=pd.read_excel(file_data,"ESTUDIANTE")
        colunm_names_df=set(df_student.columns.values)
        print(colunm_names_df)

        if isinstance( df_student,pd.core.frame.DataFrame) and colunm_required.issubset(colunm_names_df):
            successful_lines=0
            lines_with_errors = 0
            existing_record = 0
            for index,row in df_student.iterrows():

                try:
                    obj = Student.objects.get(document__exact=row['documento'])
                    existing_record = existing_record +1
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
                        successful_lines = successful_lines + 1
                    else:
                        print(f"registro {index} presento datos no validos en la hoja Estudiante")
                        lines_with_errors = lines_with_errors + 1
            status_load['load_student']['successful_lines'] = successful_lines
            status_load['load_student']['lines_with_errors'] = lines_with_errors
            status_load['load_student']['existing_record'] = existing_record
            
            
        else:
             print("NO SE PUEDE COMPROBAR EL DF")
        
    except Exception as error_plan:
        pass    

@task_success.connect(sender=loadStudent)
def loadTeacher(sender=None, args=None, file_data=None, **kwargs):
    print("#########------Este es el sender STUDENT  ------########")
    print(sender)
    
    colunm_required={'nombre','apellido','documento','edad','email','genero','direccion','salario'}
    try:
            
        df_teacher = pd.read_excel(file_data,"PROFESOR")
        colunm_names_df=set(df_teacher.columns.values)
        if isinstance( df_teacher,pd.core.frame.DataFrame) and colunm_required.issubset(colunm_names_df):
            successful_lines = 0
            lines_with_errors = 0
            existing_record = 0

            for index,row in df_teacher.iterrows():

                try:
                    obj = Teacher.objects.get(document__exact=row['documento'])
                    existing_record = existing_record +1
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
                        successful_lines = successful_lines + 1
                    else:
                        
                        lines_with_errors = lines_with_errors + 1

            status_load['load_teacher']['successful_lines'] = successful_lines
            status_load['load_teacher']['lines_with_errors'] = lines_with_errors
            status_load['load_teacher']['existing_record'] = existing_record
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
            successful_lines=0
            lines_with_errors = 0
            existing_record = 0
            for index,row in df_course.iterrows():

                try:
                    obj = Course.objects.get(name__iexact=row['nombre'])
                    existing_record = existing_record +1
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
                            successful_lines = successful_lines + 1
                        else:
                            lines_with_errors = lines_with_errors + 1

                    except Teacher.DoesNotExist:

                        lines_with_errors = lines_with_errors + 1
            
            status_load['load_course']['successful_lines'] = successful_lines
            status_load['load_course']['lines_with_errors'] = lines_with_errors
            status_load['load_course']['existing_record'] = existing_record
            
            return status_load
        
    except Exception as error_plan:
        pass 
    

task_success.connect(sender=loadCourse)
def loadScores(sender=None, args=None, file_data=None, **kwargs):

    colunm_required={'calificacion','curso','documentoEstudiante'} 
    try:
        df_scores = pd.read_excel(file_data,"CALIFICACIONES")
        colunm_names_df=set(df_scores.columns.values)

        if isinstance( df_scores,pd.core.frame.DataFrame) and colunm_required.issubset(colunm_names_df):
            successful_lines=0
            lines_with_errors = 0
            existing_record = 0
            for index,row in df_scores.iterrows():       
                try:
                    student_obj = Student.objects.get(document__exact=row['documentoEstudiante'])
                    course_obj = Course.objects.get(name__iexact=row['curso'])
                    
                    if (student_obj and course_obj and ValidatorField.RangeScores(row['calificacion'])):
                        obj = Score(course_id=course_obj, 
                                student_id=student_obj,
                                final_score=row['calificacion'],
                                )
                        obj.save()
                        successful_lines= successful_lines +1
                    else:
                        print('no existe estudiantes y profesores con los datos del registro')
                        lines_with_errors = lines_with_errors + 1
                        
                except Exception:
                    
                    print("registro a novedades de importacion")
                    lines_with_errors = lines_with_errors + 1
            
            status_load['load_scores']['successful_lines'] = successful_lines
            status_load['load_scores']['lines_with_errors'] = lines_with_errors
            status_load['load_scores']['existing_record'] = existing_record

            print(status_load)
        
    except Exception as error_plan:
        pass 



task_success.connect(sender=loadScores)
def sendEmailAboutImporter(sender=None, args=None, **kwargs):
    pass
    msg = MIMEMultipart()
    message = json.dumps(status_load)

    # setup the parameters of the message 
    password = "notificador12345"
    msg['From'] = "notificadorlsv@hotmail.com"
    msg['To'] = "efuentesramos79@gmail.com"
    msg['Subject'] = "Status Importer"
    # add in the message body 
    msg.attach(MIMEText(message, 'plain'))
    #create server 
    server = smtplib.SMTP('smtp.office365.com: 587')
    server.starttls()
    # Login Credentials for sending the mail 
    server.login(msg['From'], password,initial_response_ok = True)
    # send the message via the server. 
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()
  

@app.task
def scrapCourse():
    
    res = requests.get('https://grow.google/intl/es/courses-and-tools/?category=career&topic=cloud-computing')
    #res = requests.get(url)


    res.raise_for_status()

    course_googleSoup = bs4.BeautifulSoup(res.text, 'html.parser')

    courses = course_googleSoup.select('a[data-gtm-tag="course-card"]')


    for course in courses:

        name_course=course.find(class_='glue-headline').text
        description_course=course.find(class_='glue-card__description').text

        try:
            obj = Course.objects.get(name__iexact=name_course)
        except Course.DoesNotExist:

            obj = Course(name=name_course, 
                description=description_course,
                
            )
            obj.save()
