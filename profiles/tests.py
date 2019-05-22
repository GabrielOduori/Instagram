from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile, Image, Comment


class ProfileTestClass(TestCase):
    
    '''
    Set up method
    '''
    def setUp(self):
        self.new_profile = Profile(1,
                                   profile_photo="kenya.jpg",
                                   bio="great bio here")
    '''
    Testing instance
    '''
    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile,Profile))


    # def test_save_profile(self):
    #     self.new_profile.save_profile()
    #     check_profiles = Profile.objects.all()
    #     self.assertTrue(len(check_profiles)>0)

    # def test_delete_profile(self):
    #     self.check_profiles.delete_profile()
    #     deleted_profile=Profile.objects.all()
    #     self.assertEqual(len(deleted_profile),0)

class ImageTestClass(TestCase):
    
    '''
    Creating a new Image and saving it
    '''
    
    def setUp(self):

        self.new_image = Image(created_on='2019-05-21 08:26:19.580874',
                              image_name = 'Amboseli',
                              image='kenya.jpg',
                              image_caption = 'A great image here',
                            id=1)

    def test_image_save(self):
        self.new_image.save_image()
        allImages=Image.objects.all()
        self.assertTrue(len(allImages)>0)
        
        
    def test_delete_image(self):
        self.new_image.delete_image()
        no_image=Image.objects.all()
        self.assertTrue(len(no_image)<1)
        
        


# THIS PART DONT RUN
        
class CommentTestClass(TestCase):
    
    def setUp(self):
        
        self.new_comment = Comment(1,
                                   1,
                                   body ='The first comment', 
                                   created_on='2019-05-21 08:26:19.580874')
        self.new_comment.save_comment()
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment,Comment))
        
        
                   
#     def test_save_comment(self):
#         self.new_comment.save_comment()
#         allcomments = Comment.objects.all()
#         self.assertEqual(len(allcomments)>0)
        
    

        
    