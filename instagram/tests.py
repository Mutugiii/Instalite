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

    def test_search_by_profile_name(self):
        '''Test class for test search by profile username test case'''
        self.test_profile.save_class()
        profiles = Profile.search_profile('Test')
        self.assertTrue(len(profiles) == 1)
    
    def test_get_profile_by_id(self):
        '''Test getting a profile by it's id'''
        self.test_profile.save_class()
        profile = Profile.get_profile_by_id(self.test_profile.id)
        self.assertEqual(self.test_profile.username, profile.username)

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

    def test_get_post_by_id(self):
        '''Test getting a profile by it's id'''
        self.test_post.save_class()
        post = Post.get_post_by_id(self.test_post.id)
        self.assertEqual(self.test_post.post_caption, post.post_caption)

    def test_get_user_posts(self):
        '''Test getting all the posts by a specific user'''
        self.test_post.save_class()
        self.test_post = Post(post_caption='Another a time to be alive',user_profile = self.test_profile)
        self.test_post.save_class()
        posts = Post.get_user_posts(self.test_profile.username)
        self.assertTrue(len(posts) == 2)

class TestComment(TestCase):
    '''Test Class for Comment Class'''
    def setUp(self)-> None:
        '''To set up test class before running every test case'''
        self.test_profile = Profile(username = 'Test', bio = 'This is just a test user')
        self.test_profile.save_class()
        self.test_post = Post(post_caption='What a time to be alive',user_profile = self.test_profile)
        self.test_post.save_class()
        self.test_comment = Comment(comment = 'This is a test comment I think', comment_post = self.test_post, comment_profile = self.test_profile)
    
    def tearDown(self) -> None:
        '''To clean up after running every testcase'''
        Comment.objects.all().delete()

    def test_isinstance(self):
        '''To test if object is an instance of Class'''
        self.assertTrue(isinstance(self.test_comment, Comment))

    def test_save_comment(self):
        '''To test saving the comment'''
        self.test_comment.save_class()
        comments = Comment.objects.all()
        self.assertTrue(len(comments) == 1)

    def test_delete_comment(self):
        '''To test deleting a comment'''
        self.test_comment.save_class()
        self.test_comment.delete_class()
        comments = Comment.objects.all()
        self.assertTrue(len(comments) == 0)

    def test_update_comment(self):
        '''Test the comment updating'''
        self.test_comment.save_class()
        self.test_comment.update_class(comment = 'This is an updated comment')
        self.assertEqual(self.test_comment.comment, 'This is an updated comment')

class TestLike(TestCase):
    '''Test Class for Like Class'''
    def setUp(self)-> None:
        '''To set up test class before running every test case'''
        self.test_profile = Profile(username = 'Test', bio = 'This is just a test user')
        self.test_profile.save_class()
        self.test_post = Post(post_caption='What a time to be alive',user_profile = self.test_profile)
        self.test_post.save_class()
        self.test_like = Like(value = 12, user = self.test_profile, post = self.test_post)
    
    def tearDown(self) -> None:
        '''To clean up after running every testcase'''
        Like.objects.all().delete()

    def test_isinstance(self):
        '''To test if object is an instance of Class'''
        self.assertTrue(isinstance(self.test_like, Like))

    def test_save_like(self):
        '''To test saving the like'''
        self.test_like.save_class()
        likes = Like.objects.all()
        self.assertTrue(len(likes) == 1)

    def test_delete_like(self):
        '''To test deleting a like'''
        self.test_like.save_class()
        self.test_like.delete_class()
        likes = Like.objects.all()
        self.assertTrue(len(likes) == 0)

    def test_update_like(self):
        '''Test the like updating'''
        self.test_like.save_class()
        self.test_like.update_class(like = 'This is an updated like')
        self.assertEqual(self.test_like.like, 'This is an updated like')
