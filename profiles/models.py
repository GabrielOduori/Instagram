from django.db import models

# Create your models here.
class Profile(models.Model):
    profilePhoto = models.ImageField(upload_to = 'profilePhotos')
    bio = models.CharField(max_length = 200)
    
    
    
class Image(models.Model):
     imageDate = models.DateTimeField(auto_now_add=True)
     imageName = models.CharField(max_length = 100)
     photoImage = models.ImageField(upload_to  ='postedImages')
     imageCaption = models.TextField()
     profileId = models.ForeignKey(Profile)
     
     
     def __str__(self):
         pass
     def save_image(self):
         pass
     
     def save_image(self):
         pass
         
     def save_image(self):
             pass
       
class Comment(models.Model):
    imageId = models.ForeignKey(Image)
    profileID  =  models.ForeignKey(Profile)
    comment = models.CharField(max_length=300)
    commentDate = models.DateTimeField(auto_now_add=True)

  
class Like(models.Model):
    likeDate = models.DateTimeField(auto_now_add=True)
    imageID  =  models.ForeignKey(Image)# Id of the person who likes the post
    profileID  =  models.ForeignKey(Profile)



class Follow(models.Model):
    followDate = models.DateTimeField(auto_now_add=True)
    followerID = models.ForeignKey(Profile)

