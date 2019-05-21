from django.contrib import admin
from profiles.models import Profile, Image, Comment

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user']
    
    
class ImageAdmin(admin.ModelAdmin):
    list_display = ['created_on','image_name']
    
    
class CommentAdmin(admin.ModelAdmin):
    list_display = ['body','author' ,'created_on']
    
    
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Comment, CommentAdmin)