from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Image, Comment, Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    
        
class UploadImageForm(forms.ModelForm):
    class Meta:
        model  =  Image
        
        fields = [
            
            'image_name',
            'image_caption',
            'image',
        ]
        
        
        
        
class CommentForm(forms.Form):
    author = forms.CharField(max_length=60, widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Your Name"
        })
    )
    body = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Leave a comment!"
        })
    )
            
        
        
class EditUserProfile(UserChangeForm):
    
        class Meta:
            model  = Profile
            fields = [
                'bio',
                'profile_photo',
                'password'
                
            ]