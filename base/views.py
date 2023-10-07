from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.contrib import messages
from django.db.models import Q
from .models import *
from .forms import *

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        tutorials=Tutorial.objects.all()
        your_tutorials = Tutorial.objects.filter(user=request.user.profile)
        context={'user':request.user,'tutorials':tutorials,'your_tutorials':your_tutorials}
        return render(request,'base/home.html',context)
    else:
        tutorials=Tutorial.objects.all()
        user=[]
        context={'tutorials':tutorials,'user':user}
        return render(request,'base/home2.html',context)
def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password=request.POST.get('password')
        try :
            user = User.objects.get(username=username)
        except:
            messages.error(request, "user does not exist")
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request, "username or password does not exist")
    return render(request,'base/login-page.html')

def createaccount(request):
    form=CreateUserForm()
    context={'form':form}
    if request.method == 'POST':
        form=CreateUserForm(request.POST)
        if form.is_valid :
            user = form.save(commit=False)
            user.save()
            login(request,user)
            return redirect('home')
    return render(request,'base/create-account.html',context)
def profilepage(request,profile_id):
    profile=Profile.objects.get(id=profile_id)
    user=profile.user
    try:
        tutorials=Tutorial.objects.filter(user=profile)
    except :
        tutorials=[]
    context={'profile':profile,'tutorials':tutorials}
    return render(request,'base/profile-page.html',context)
def logoutpage(request):
    logout(request)
    return redirect('home')
def editprofile(request,profile_id):
    profile=Profile.objects.get(id=profile_id)
    form=UpdateUserForm(instance=profile)
    if request.method == 'POST':
        form = UpdateUserForm(request.POST,request.FILES,instance=profile)
        if form.is_valid:
            form.save()
            return redirect('profile-page',profile_id=profile.id)
    context={'form':form}
    return render(request,'base/edit-profile.html',context)
def createtutorial(request):
    form=TutorialCreationForm()
    profile=request.user.profile
    if request.method == 'POST':
        form=TutorialCreationForm(request.POST,request.FILES)
        if form.is_valid:
            tutorial=Tutorial.objects.create(
                user=profile,
                name=request.POST.get('name'),
                cover=request.FILES['cover'],
                description=request.POST.get('description'),
                price=request.POST.get('price')
            )
            tutorial.save()
            # tutorial=form.save()
            # tutorial.user=user
            return redirect('home')
    context={'form':form}
    return render(request,'base/create-tutorial.html',context)
def tutorialpage(request,tutorial_id):
    tutorial=Tutorial.objects.get(id=tutorial_id)
    try :
        videos=tutorial.video_set.all()
    except :
        videos=[]
    MEDIA_URL='/media/videos/'
    context={'tutorial':tutorial,'videos':videos,'MEDIA_URL':MEDIA_URL}
    return render(request,'base/tutorial-page.html',context)
def createvideo(request,tutorial_id):
    form=VideoForm()
    tutorial=Tutorial.objects.get(id=tutorial_id)
    if request.method == 'POST':
        form=VideoForm(request.POST,request.FILES)
        if form.is_valid:
            video=Video.objects.create(
                title=request.POST.get('title'),
                video=request.FILES['video'],
                description=request.POST.get('description'),
                tutorial=tutorial
            )
            video.save()
            return redirect('tutorial-page',tutorial_id)
    context={'form':form}
    return render(request,'base/add-video.html',context)
def tutorials(request):
    q=request.GET.get('q') if request.GET.get('q') is not None else ''
    user=request.user
    tutorials=Tutorial.objects.filter(Q(name__icontains=q))
    context={'user':user,'tutorials':tutorials}
    return render(request,'base/tutorials.html',context)
    