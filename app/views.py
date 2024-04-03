from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.
def insert_topic(request):
    ETFO=TopicForm()
    d={'ETFO':ETFO}

    if request.method=='POST':
        TFDO=TopicForm(request.POST)

        if TFDO.is_valid():
            TFDO.save()
            return HttpResponse('Data is inserted Successfully...!')
        
    return render(request,'insert_topic.html',d)

def insert_webpage(request):
    EWFO=WebpageForm()
    d={'EWFO':EWFO}

    if request.method=='POST':
        WFDO=WebpageForm(request.POST)

        if WFDO.is_valid():
            WFDO.save()
            return HttpResponse('Webpage Data is inserted successfully...!!!')
        
    return render(request,'insert_webpage.html',d)

def insert_accessrecord(request):
    EAFO=AccessRecorsForm()
    d={'EAFO':EAFO}

    if request.method=='POST':
        AFDO=AccessRecorsForm(request.POST)

        if AFDO.is_valid():
            AFDO.save()
            return HttpResponse('AccessRecord Data is inserted Successfully!!!')
        
    return render(request,'insert_accessrecord.html',d)