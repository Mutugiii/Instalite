from django import forms
from django.contrib.auth.forms import UserCreationForm
from cloudinary.forms import CloudinaryFileField
from django.contrib.auth.models import User
from .models import Profile, Post, Comment

class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class UpdateBioForm(forms.ModelForm):
    profile_photo = CloudinaryFileField(
        options = {
            'folder': 'instagram'
       }
    )
    class Meta:
        model = Profile
        exclude = ['follower', 'following', 'joined', 'user']

class PostForm(forms.ModelForm):
    post_image = CloudinaryFileField(
        options = {
            'folder': 'instagram'
       }
    )
    class Meta:
        model = Post
        exclude = ['user_profile', 'likes', 'published']
        fields = ('post_caption', 'post_image')