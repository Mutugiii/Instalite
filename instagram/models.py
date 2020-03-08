from django.db import models
from django.contrib.auth.models import User

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

class Comment(models.Model, CrudMethods):
    '''Method to allow user comments'''
    comments = models.TextField()

    def __str__(self):
        return self.comments

class Profile(models.Model, CrudMethods):
    '''Model class for the user and his profile'''
    username = models.CharField(max_length=30)
    bio = models.TextField(blank=True)
    profile_photo = models.ImageField(upload_to='images/', blank=True)
    follower = models.ForeignKey(User, related_name='following', blank=True, on_delete=models.CASCADE)
    following = models.ForeignKey(User, related_name='followers', blank=True, on_delete=models.CASCADE)
    joined = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('follower', 'following')

    def __str__(self):
        return '{} follows {}'.format(self.follower,self.following)

class Post(models.Model, CrudMethods):
    '''Models Class to implement publishing of new posts/content'''
    post_caption = models.TextField()
    post = models.CharField
    image_link = models.ImageField(upload_to='images/', blank=True)
    user_profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    likes = models.IntegerField()
    comments = models.ManyToManyField(Comment)
    published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post
        
class Like(models.Model, CrudMethods):
    '''Model class to allow users to like photos'''
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    value = models.IntegerField(blank=True)

    def __str__(self):
        return self.value