from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.
def insert_topic(request):
    form=TopicForm()
    d={'form':form}

    if request.method=='POST':
        form_data=TopicForm(request.POST)
        if form_data.is_valid():
            form_data.save()

            return HttpResponse('topic model from is created by using model')
    return render(request,'insert_topic.html',d)

        
def insert_Webpage(request):
    form=WebpageForm()
    d={'form':form}

    if request.method=='POST':
        form_data=WebpageForm(request.POST)
        if form_data.is_valid():
            form_data.save()

            return HttpResponse('Webpage model from is created by using model')
    return render(request,'insert_Webpage.html',d)

def insert_AccessRecords(request):
    form=AccessRecordsForm()
    d={'form':form}

    if request.method=='POST':
        form_data=AccessRecordsForm(request.POST)
        if form_data.is_valid():
            form_data.save()

            return HttpResponse('AccessRecords model from is created by using model')
    return render(request,'insert_AccessRecords.html',d)        