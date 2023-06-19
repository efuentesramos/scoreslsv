from django.shortcuts import render,redirect
from .forms import uploaderForm,scrapperForm
import pandas as pd
import base64
from .models import Student,Teacher,Course,Score
from apps.training.utils.validator import ValidatorField
from apps.training.tasks import  loadStudent,loadTeacher,loadCourse, loadScores, scrapCourse

# Create your views here.

def Home(request):
    
    return render(request ,'index.html')

def Processing (request):

    return render(request,'training/in_process.html')

def loadCourseFramPage (request):

    if request.method== 'POST':
        scrapper_form=scrapperForm(request.POST)
        
        scrapCourse.delay()

        return redirect('processing')
    else:
        pass
        
        scrapper_form=scrapperForm()
    
    
    return render(request,'training/scrapping_course.html',{'scrapper_form':scrapper_form})


def uploaderInfo(request):

    if request.method== 'POST' and request.FILES:
        uploader_form=uploaderForm(request.POST)
        
        file=request.FILES['file_score_info']
        content=file.read()


        loadStudent.delay(content)
        
        loadTeacher(file_data=content)

        loadCourse(file_data=content)

        loadScores(file_data=content)

    
        return redirect('processing')

    else:
        pass
        uploader_form=uploaderForm()
    
    return render(request,'training/load_info.html',{'uploader_form':uploader_form})
