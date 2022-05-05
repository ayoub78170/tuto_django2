from tkinter.tix import Form
from urllib import response
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request,):
    return HttpResponse('index Users !')

#def detail(request):
    #return HttpResponse('Detail User')

def detail(request, user_id):
    reponse="vous regadez les users %s."
    return HttpResponse(reponse %user_id)

