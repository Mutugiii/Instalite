from django.shortcuts import render, loader, redirect
from django.http import HttpResponse
from .models import Post, Profile, Comment, Like
from .forms import SignUpForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def index(request):
    '''View Function for the Main page'''
    template = loader.get_template('index.html')
    context = {
        'message': 'Welcome'
    }
    return HttpResponse(template.render(context, request))

def signup(request):
    '''View Function for user signup'''
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    template = loader.get_template('registration/signup.html')
    context = {
        'form': form
    }
    return HttpResponse(template.render(context, request))

def logout_user(request):
    logout(request)

    return redirect(index)
