from django.shortcuts import render, loader, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Post, Profile, Comment, Like, Follow
from .forms import SignUpForm, UpdateBioForm, PostForm, CommentForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .email import send_welcome_email

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
            user.save()
            login(request, user)
            profile = Profile(username = user.username, user = request.user)
            profile.save()
            send_welcome_email(request.user.username, request.user.email)
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
    user = get_object_or_404(User, username = request.user.username)
    profile = Profile.objects.filter(username = request.user.username).first()
    posts = Post.get_user_posts(request.user.username)
    followers = Follow.objects.filter(following=user.profile)
    following = Follow.objects.filter(follower=user.profile)
    template = loader.get_template('profile/profile.html')
    context = {
        'profile': profile,
        'posts': posts,
        'followers': followers,
        'following': following,
    }
    return HttpResponse(template.render(context, request))

@login_required(login_url='/login/')
def update_profile(request, profile_id):
    '''View Function to update user profile'''
    current_user = request.user
    if request.method == 'POST':
        form = UpdateBioForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                Profile.get_profile_by_id(profile_id)
                profile = form.save(commit=False)
                profile.save()
            except ValueError:
                return redirect('index')
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

@login_required(login_url='/login/')
def search(request):
    '''View Function to search for users'''
    if 'searchusers' in request.GET and request.GET['searchusers']:
        search_term = request.GET.get('searchusers')
        users = Profile.search_profile(search_term)
        template = loader.get_template('profile/search.html')
        context = {
            'users': users
        }
        return HttpResponse(template.render(context, request))  
    else:
        return redirect('index')

@login_required(login_url='/login/')
def other_profile(request, user_name):
    '''View function to show other users profile'''
    user = get_object_or_404(User, username = user_name)
    if request.user == user:
        return redirect('profile')
    posts = Post.get_user_posts(user_name)
    followers = Follow.objects.filter(following=user.profile)
    following = Follow.objects.filter(follower=user.profile)
    follow_status = None
    for follower in followers:
        if request.user.profile == follower.follower:
            follow_status = True
        else:
            follow_status = False
    template = loader.get_template('profile/other.html')
    context = {
        'profile': user,
        'posts': posts,
        'status': follow_status,
        'followers': followers,
        'following': following,
    }
    return HttpResponse(template.render(context, request))

@login_required(login_url='/login/')
def specificpost(request, post_id):
    '''View function to view a specific post'''
    post = Post.get_post_by_id(post_id)
    comments = Comment.get_post_comments(post_id)
    template = loader.get_template('posts/specific.html')
    context = {
        'comments': comments,
        'post': post
    }
    return HttpResponse(template.render(context, request))

@login_required(login_url='/login/')
def comments(request, post_id):
    '''View function to write a comment to a post'''
    post = Post.get_post_by_id(post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.comment_post = post
            comment.save()
            return redirect('specificpost', post_id)
    else:
        form = CommentForm()
    template = loader.get_template('posts/add_comment.html')
    context = {
        'form': form,
    }
    return HttpResponse(template.render(context, request))

@login_required(login_url='/login/')
def follow(request,user_id):
    '''View Function to follow users'''
    if request.method == 'GET':
        user = Profile.get_profile_by_id(user_id)
        tofollow = Follow(follower = request.user.profile , following = user)
        tofollow.save()
        return redirect('otherprofile', user.username)
    else:
        return redirect('profile')

@login_required(login_url='/login/')
def unfollow(request, user_id):
    '''View function to unfollow users'''
    if request.method == 'GET':
        user = Profile.get_profile_by_id(user_id)
        delete_true = Follow.unfollow_user(request.user.profile, user)
        if delete_true == True:
            return redirect('otherprofile', user.username)
    else:
        return redirect('profile')