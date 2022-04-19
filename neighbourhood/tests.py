
from django.test import TestCase
from .models import Profile, Post

# Create your tests here.
class EditorTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.pascal= Profile(neighbourhood_name = 'paclas', username ='pascalouma54@gmail.com')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.pascal,Post))

        # Testing Save Method
    def test_save_method(self):
        self.pascal.save_post()
        posts = Post.objects.all()
        self.assertTrue(len(posts) > 0)

class ProfileTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.pascal= Profile(neighbourhood_name = 'paclas', username ='pascalouma54@gmail.com')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.pascal,Post))

        # Testing Save Method
    def test_save_method(self):
        self.pascal.save_post()
        posts = Post.objects.all()
        self.assertTrue(len(posts) > 0)


class BusinessTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.pascal= Profile(neighbourhood_name = 'paclas', username ='pascalouma54@gmail.com')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.pascal,Post))

        # Testing Save Method
    def test_save_method(self):
        self.pascal.save_post()
        posts = Post.objects.all()
        self.assertTrue(len(posts) > 0)