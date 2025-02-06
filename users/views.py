from django.shortcuts import render, redirect
from . models import Profile,Message
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm, ProfileForm, SkillForm, MessageForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.urls import reverse




# Create your views here.

def profiles(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    
    profiles = Profile.objects.filter(Q(name__icontains = search_query) | Q(short_intro__icontains = search_query))
    return render(request, 'users/profiles.html', {'profiles': profiles, 'search_query':search_query})

def profile(request, pk):
    profile = Profile.objects.get(id = pk)
    return render(request, 'users/user_profile.html', {'profile': profile})


def user_login(request):

    page = 'login'

    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exists')
            return redirect('login')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(request.GET['next'] if 'next' in request.GET else reverse('user_account'))

        else:
            messages.error(request, 'Password is incorrect')
        
    return render(request, 'users/login_register.html',{'page':page})



def register(request):

    page = 'register'
    # form = UserCreationForm()
    form = CustomUserCreationForm()

    if request.method == 'POST':

        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()  # here we save and store that instance in user so when user is created then also login 
            messages.success(request, 'User acccout was created')
            login(request,user)  # here we use that user instance
            return redirect('edit_account_form')
        else:
            messages.error(request,'please fill correct details')
        

    return render(request, 'users/login_register.html', {'page':page, 'form':form})



def user_logout(request):

    logout(request)
    messages.info(request, 'User was succesfully logout')
    return redirect('profiles')

@login_required(login_url='login')
def user_account(request):
    profile = request.user.profile
    return render(request, 'users/account.html', {'profile':profile})


@login_required(login_url='login')
def edit_account_form(request):
    profile = Profile.objects.get(user=request.user)   # profile = request.user.profile both are same because one to one 
    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request,'Profile Updated succesfully')
            return redirect('user_account')

    return render(request, 'users/edit_account_form.html', {'form':form})


@login_required(login_url='login')
def skill_form(request):
    profile = request.user.profile
    print('profile', profile)
    form = SkillForm()

    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            user_skill = form.save(commit=False)
            user_skill.owner = profile
            user_skill.save()
            messages.success(request,'New skill added succesfully')
            return redirect('user_account')

    return render(request, 'users/skill_form.html',{'form':form})

@login_required(login_url='login')
def update_skill_form(request,pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id = pk)
    form = SkillForm(instance=skill)

    if request.method == 'POST':
        form = SkillForm(request.POST,instance=skill)
        if form.is_valid():
            form.save()
            messages.success(request,'skill updated succesfully')
            return redirect('user_account')

    return render(request, 'users/update_skill.html',{'form':form,'pk':pk})


@login_required(login_url='login')
def delete_skill(request,pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id = pk)
    if request.method == 'POST':
        skill.delete()
        messages.success(request,'skill deleted succesfully')
        return redirect('user_account')

    return render(request, 'myprojects/delete_project.html',{'project':skill})


@login_required(login_url='login')
def inbox(request):
    profile = request.user.profile
    Relatedmessages = profile.messages.all()
    countUnRead = Relatedmessages.filter(is_read = False).count()
    data = {
        'Relatedmessages':Relatedmessages,
        'countUnRead':countUnRead
    }
    return render(request, 'users/inbox.html', data)

@login_required(login_url='login')
def view_message(request,pk):
    msg = Message.objects.get(id = pk)
    if msg.is_read == False:
        msg.is_read = True
        msg.save()

    data ={
        'msg':msg
    }
    return render(request, 'users/message.html',data)


@login_required(login_url='login')
def create_message(request,pk):
    receiver = Profile.objects.get(id = pk)
    form = MessageForm()

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            msg = form.save(commit=False)
            msg.sender = request.user.profile
            msg.receiver = receiver
            msg.save()
            messages.success(request, 'Message sent succesfully')
            return redirect('profile', pk=receiver.id)

    data = {
        'receiver': receiver,
        'form':form
    }
    return render(request, 'users/message_form.html',data)
