from django.shortcuts import render, loader
from django.http import HttpResponse

def index(request):
    '''View Function for the Main page'''
    template = loader.get_template('index.html')
    context = {
        'message': 'Welcome'
    }
    return HttpResponse(template.render(context, request))
