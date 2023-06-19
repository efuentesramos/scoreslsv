from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=100,null=True,blank=True)
    email = models.EmailField(max_length=50)
    age = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(120)],null=True,blank=True)
    
    document = models.PositiveIntegerField(unique=True)
    
    GENDER = [
        ("M","Masculino"),
        ("F","Femenino"),
        
    ]
    gender = models.CharField(
        max_length=2,
        choices=GENDER,
    )

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Student(Person):
    
    hobbies = models.TextField(max_length=200,null=True,blank=True)

class Teacher(Person):
    
    salary = models.PositiveIntegerField(null=True,blank=True)

class Course(models.Model):
    
    name = models.CharField(max_length=50,unique=True)    
    
    total_hours = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(500)])
    
    description = models.TextField(max_length=500,null=True,blank=True)
    
    teacher_id = models.ForeignKey(Teacher,
                                on_delete=models.CASCADE,)
    
    def __str__(self):
        return self.name
    
class Score(models.Model):

    course_id = models.ForeignKey(Course,
                                on_delete=models.CASCADE,)
    student_id = models.ForeignKey(Student,
                                on_delete=models.CASCADE,)
    final_score = models.DecimalField(max_digits=3, decimal_places=2)

    def __str__(self):
        return str(self.final_score)
    




