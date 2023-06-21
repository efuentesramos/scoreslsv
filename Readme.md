
## Scores lsv
El proyecto consiste en  una aplicación Django  que permita importar y gestionar datos relacionados con los estudiantes, profesores, cursos, calificaciones. Se utiliza Celery para procesar las importaciones masivas de datos, tambien  se implementa un scrapper para obtener información adicional sobre los cursos desde una fuente externa.

### Requisitos

El proyecto se soporta principalmente de Django(4.2.2), Django-restframework (3.14.0), Celery (5.3.0) y RRabbitMQ.
Las librerias complementarias estan especificadas en el archivo requirements.txt contenido en la raiz del proyecto.

### Uso

A cotinuacion se especifican las url para tener acceso a la carga de informacion  y API :

http://127.0.0.1:8000/training/load_info :  

Desde esta URL se puede cargar masiva de informacion para poblar la BD con el archivo plantilla  info_scoresBD.xlsx 


http://127.0.0.1:8000/training/courses_load/ :  

Desde esta URL se puede cargar informacion adicional acerca de cursos y poblar la tabla de cursos ,extrayendo informacion desde el sitio web
https://grow.google/intl/es/courses-and-tools/?category=career&topic=cloud-computing


#### Endpoint API

http://127.0.0.1:8000/student/student/ : Listado de estudiantes

http://127.0.0.1:8000/student/student/<documento_estudiante>/ : Detalle de los datos de un estudiante

http://127.0.0.1:8000/teacher/teacher/   : Listado de profesores

http://127.0.0.1:8000/teacher/teacher/<documento_profesor>/  : Detalle de los datos de un profesor

http://127.0.0.1:8000/course/course/  : Listado de curso

http://127.0.0.1:8000/course/course/<nombre_curso>/ : Detalle de un curso

http://127.0.0.1:8000/score/score/    : Lista todas las notas registras


http://127.0.0.1:8000/score/score/<documento_estudiante>/<nombre_curso>/ : Calificación especifica de un estudiante en un curso

http://127.0.0.1:8000/score/score/<documento_estudiante>/ : Calificaciones que tiene un estudiante en sus cursos


#### Notificaciones

Las notificaciones se realizan desde el siguiente correo : notificadorlsv@hotmail.com
 
y se recepcionan a traves del Email : notificadorlsv@gmail.com




