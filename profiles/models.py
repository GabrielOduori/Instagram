from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    '''
    The Profile Model inherits from the User model 
    from from django.contrib.auth.models
    '''
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    profile_photo = models.ImageField(default='default.jpg',upload_to = 'profilePhotos')
    bio = models.CharField(max_length = 200)
    
    def __str__(self):
        return f'{self.user.username}'
    
    # class Meta:
    #     verbose_name = 'Profile'
    #     verbose_name_plural = 'Profiles'
    

       
  
# class Like(models.Model):
#     likeDate = models.DateTimeField(auto_now_add=True)
#     image  =  models.ForeignKey(Image)# Id of the person who likes the post
#     profile  =  models.ForeignKey(Profile)


# class Follow(models.Model):
#     followDate = models.DateTimeField(auto_now_add=True)
#     followerID = models.ForeignKey(Profile)

class Image(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    image_name = models.CharField(max_length = 100)
    image = models.ImageField(upload_to  ='postedImages')
    image_caption = models.TextField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
     
     
    def __str__(self):
        return f'{self.image_name}'
     
     
    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'
         
    def save_image(self):
        self.save()
     
    def delete_image(self):
        self.delete()
        
        
    @classmethod
    def search_users(cls,term):
        result=cls.objects.filter(user__username__icontains=term)
        return result

     
     
class Comment(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='comments')
    author  =  models.ForeignKey(Profile, on_delete=models.CASCADE)
    body = models.CharField(max_length=300)
    created_on = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f'{self.body}'
     
    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        
        
    def save_comment(self):
        self.save()
        
        
    def delete_comment(self):
        self.delete()
        
         
