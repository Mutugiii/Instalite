from django.shortcuts import render, loader, redirect
from django.http import HttpResponse
from .models import Post, Profile, Comment, Like
from .forms import SignUpForm, UpdateBioForm, PostForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def index(request):
    '''View Function for the Main page'''
    template = loader.get_template('index.html')
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return HttpResponse(template.render(context, request))

def signup(request):
    '''View Function for user signup'''
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = Profile(username = user.username)
            profile.save()
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

@login_required(login_url='/login/')
def profile(request):
    '''User profile view'''
    profile = Profile.objects.filter(username = request.user.username).first()
    posts = Post.get_user_posts(request.user.username)
    template = loader.get_template('profile/profile.html')
    context = {
        'profile': profile,
        'posts': posts
    }
    return HttpResponse(template.render(context, request))

@login_required(login_url='/login/')
def update_profile(request):
    '''View Function to update user profile'''
    current_user = request.user
    # profile = Profile.objects.filter(username = request.user.username).first()
    if request.method == 'POST':
        form = UpdateBioForm(request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data['username']
            bio = form.cleaned_data['bio']
            user = request.user
            profile = Profile.objects.filter(username = user.username).update(username = username, bio=bio, user = user)
            return redirect('profile')
    else:
        form = UpdateBioForm()
    template = loader.get_template('profile/updateprofile.html')
    context = {
        'form': form
    }
    return HttpResponse(template.render(context, request))

@login_required(login_url='/login/')
def upload_post(request):
    '''View function to upload a post'''
    current_user = request.user
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
            return redirect('index')
    else:
        form = PostForm()
    template = loader.get_template('posts/post.html')
    context = {
        'form': form
    }
    return HttpResponse(template.render(context, request))  