from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Post, Comment

class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class UpdateBioForm(forms.ModelForm):
     class Meta:
        model = Profile
        exclude = ['follower', 'following', 'joined', 'user']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user_profile', 'likes', 'published']