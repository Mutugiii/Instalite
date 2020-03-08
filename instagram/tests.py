from django.test import TestCase
from .models import Comment, Profile, Post, Like

class TestProfile(TestCase):
    '''Test Class to test the Profile Class'''
    def setUp(self)-> None:
        '''To set up test class before running every test case'''
        self.test_profile = Profile(username = 'Test', bio = 'This is just a test user')
    
    def tearDown(self) -> None:
        '''To clean up after running every testcase'''
        Profile.objects.all().delete()

    def test_isinstance(self):
        '''To test if object is an instance of Class'''
        self.assertTrue(isinstance(self.test_profile, Profile))

    def test_save_profile(self):
        '''To test saving the profile'''
        self.test_profile.save_class()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) == 1)

    def test_delete_profile(self):
        '''To test deleting profile'''
        self.test_profile.save_class()
        self.test_profile.delete_class()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) == 0)

    def test_update_profile(self):
        '''Test the profile updating'''
        self.test_profile.save_class()
        self.test_profile.update_class(username = 'newTest')
        self.assertEqual(self.test_profile.username, 'newTest')

class TestPost(TestCase):
    '''Test Class to test the Post Class'''
    def setUp(self) -> None:
        '''To set up test class before running every test case'''
        self.test_profile = Profile(username = 'Test', bio = 'This is just a test user')
        self.test_profile.save_class()
        self.test_post = Post(post_caption='What a time to be alive',user_profile = self.test_profile)

    def tearDown(self) -> None:
        '''To clean up after every test case'''
        Post.objects.all().delete()

    def test_isinstance(self):
        '''To test if object is an instance of Class'''
        self.assertTrue(isinstance(self.test_post, Post))

    def test_save_post(self):
        '''To test saving the post'''
        self.test_post.save_class()
        posts = Post.objects.all()
        self.assertTrue(len(posts) == 1)

    def test_delete_post(self):
        '''To test deleting post'''
        self.test_post.save_class()
        self.test_post.delete_class()
        posts = Post.objects.all()
        self.assertTrue(len(posts) == 0)

    def test_update_post(self):
        '''Test the post updating'''
        self.test_post.save_class()
        self.test_post.update_class(post_caption = 'You only live once')
        self.assertEqual(self.test_post.post_caption, 'You only live once')