from django.shortcuts import render, redirect
from .forms import UserRegisterForm, EditUserProfile, UploadImageForm
from django.contrib.auth import authenticate, login,logout  
from django.contrib import messages
from .models import Profile, Image, Comment
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
# from django.contrib.auth.forms import UserChangeForm



def index(request):
    title = 'Home'
    return render(request, 'index.html', {"title":title})

@login_required
def user_profile(request):
    current_user = request.user
    images =  Image.objects.filter(profile = current_user.profile)
    # image =  Image.objects.all()
    try:
        profile = Profile.objects.get(user = current_user)
        
    except: 
        ObjectDoesNotExist
    print(profile.bio)
    
    context = {
        
        'profile':profile,
        'images':images,
        'current_user':current_user
    }
        
    return render(request,'profile/profile.html', context)

    
def login_user(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request,('You have been loged in'))
            return redirect('profile')
        else:
            messages.success(request,('Error Loggin in. Plase try again!'))
            return redirect('login')
    else:
         
        return render(request,'registration/login.html',{})
    
def logout_user(request):
    logout(request)
    messages.success(request,('You have been logged out'))
    return redirect('index')
    



def register_user(request):
    if request == 'POST':
        form  = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Hi {username}, your account has been created!')
            return redirect("/profile/profile")
    else:
        form = UserRegisterForm()
        context = {'form':form}
    return render(request, 'registration/registration_form.html',context)
    

def stream(request):
    # image = Image.objects.get(pk = id)
    
    streams = Image.objects.all().order_by('-created_on')
    # comments = Comment.objects.filter()
    comments = Comment.objects.all()
    
    context = {
        "streams":streams,
        "comments":comments,
        # "image":image,
        
        }
    return render(request,'images/stream.html', context)


@login_required
def upload_image(request):
    current_user  = request.user.profile
    if request.method =='POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.profile = current_user
            image.save()
        return redirect('profile')
    else:
        form  = UploadImageForm()
        context  = {
            "form":form
            }
    return render(request, 'images/upload_image.html', context)


def image_detail(request, id):
    image = Image.objects.get(pk = id)
    return render(request, 'images/image_detail.html', {"image":image})

@login_required
def add_comment(request, id):
    image = Image.objects.get(pk = id)
    profile = request.user.profile
    body  = request.POST.get('comments_body')
    
    Comment.objects.create(image=image, author = profile, body=body)
    
    return redirect('stream')




@login_required
def edit_profile(request):
    if request == 'POST':
        form  = EditUserProfile(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            messages.success(request, f'Hi {username}, your account has been updated!')
            return redirect("/profile/profile")
    else:
        form = EditUserProfile(request.POST,instance = request.user)
        context = {'form':form}
    return render(request, 'registration/edit_profile.html',context)
    


def search_user(request):
    
    if 'user' in request.GET and request.GET['user']:
        term=request.GET.get("user")
        found=Image.search_users(term)
        message=f'{term}'
        
        context = {
            "message":message,
            "founds":found,
            "term":term
            }

        return render(request,'profile/search.html',context)
    else:
        message="Please feed in a username to be searched"
        return render(request,"profile/search.html",{"message":message})