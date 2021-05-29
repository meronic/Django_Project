from django import template
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request) : 
    template = loader.get_template('mainapp/index.html')
    context = {
        'lastest_question_list' : "test",
    }
    
    return HttpResponse(template.render(context, request))