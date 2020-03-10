from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from cloudinary.models import CloudinaryField

class CrudMethods:
    '''Method class for Common methods'''
    def save_class(self):
        '''Function to save class to database'''
        self.save()

    def delete_class(self):
        '''Function to delete class from database'''
        self.delete()

    def update_class(self, **kwargs):
        '''Function to update the class in database'''
        for key,value in kwargs.items():
            setattr(self,key,value)
            self.save()

class Profile(models.Model, CrudMethods):
    '''Model class for the user and his profile'''
    username = models.CharField(max_length=40, unique=True)
    bio = HTMLField()
    profile_photo = CloudinaryField('image')
    joined = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='profile')    

    @classmethod
    def get_profile_by_id(cls, profile_id):
        '''Classmethod to get a user by the profile id'''
        profile = Profile.objects.filter(id = profile_id).first()
        return profile

    @classmethod
    def get_profile_by_name(cls, search_name):
        '''Classmethod to get a user by the search name'''
        profile = Profile.objects.filter(username = search_name).first()
        return profile

    @classmethod
    def search_profile(cls, search_name):
        '''Classmethod to search for a profile by username'''
        profiles = Profile.objects.filter(username__icontains = search_name)
        return profiles

    def __str__(self):
        return self.username

class Post(models.Model, CrudMethods):
    '''Models Class to implement publishing of new posts/content'''
    post_caption = HTMLField()
    post_image = CloudinaryField('image')
    user_profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='posts')
    likes = models.IntegerField(default=0)
    published = models.DateTimeField(auto_now_add=True)

    @classmethod
    def get_post_by_id(cls, post_id):
        '''Classmethod to get a post by the given id'''
        post = Post.objects.filter(id = post_id).first()
        return post

    @classmethod
    def get_user_posts(cls, profile_name):
        '''Classmethod to get the posts by a given user profile'''
        posts = Post.objects.filter(user__username = profile_name)
        return posts

    def __str__(self):
        return self.post_caption
        
class Comment(models.Model, CrudMethods):
    '''Method to allow user comments'''
    comment = HTMLField()
    comment_post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    comment_profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    @classmethod
    def get_post_comments(cls, post_id):
        '''Classmethod to get the posts by a given user profile'''
        post = Comment.objects.filter(comment_post = post_id)
        return post

    def __str__(self):
        return self.comment

class Like(models.Model, CrudMethods):
    '''Model class to allow users to like photos'''
    value = models.IntegerField(blank=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return 'value: {}'.format(self.value)

class Follow(models.Model, CrudMethods):
    follower = models.ForeignKey(Profile, related_name='following', on_delete=models.CASCADE)
    following = models.ForeignKey(Profile, related_name='followers', on_delete=models.CASCADE)

    @classmethod
    def unfollow_user(self, follower, following):
        '''Class method to unfollow a user'''
        rel = Follow.objects.filter(follower = follower, following = following)
        rel.delete()
        return True

    def __str__(self):
        return f'{self.following} following {self.follower}'