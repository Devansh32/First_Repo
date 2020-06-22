from django.shortcuts import render
from  django.http import HttpResponse,HttpResponseRedirect
from app2.models import Users
from . import forms

from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout


# Create your views here.
def index(request) :
    # return HttpResponse("<b>Hello World! </b>")
    return render(request,'app2/index.html')

def user(request):

    user_list = Users.objects.order_by('f_name')
    user_dict = {'users': user_list}
    return render(request,'app2/users.html', context=user_dict)

def FF(request):
    form = forms.FormName()
    if request.method == "POST":
        form=forms.FormName(request.POST)
        if form.is_valid():
            print("submitted ")
            print(form.cleaned_data['name'])
            print(form.cleaned_data['email'])
            print(form.cleaned_data['text'])

    return render(request,'app2/form_page.html',{'form':form})

def SU(request):
    form=forms.myForm()
    if request.method == "POST":
        form = forms.myForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            # return render(request, 'app2/signup.html', {'form': form})
            return index(request)
        else:
            print("invalid form")
    return render(request, 'app2/signup.html', {'form': form})


def register(request):
    registered=False

    if request.method=="POST":
        user_form = forms.UserForm(data=request.POST)
        profile_form = forms.UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile=profile_form.save(commit=False)
            profile.user=user #one to one relationship in forms

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors,profile_form.errors)

    else:
        user_form=forms.UserForm()
        profile_form = forms.UserProfileInfoForm()

    return render(request,'app2/registration.html',
                  {'user_form':user_form,
                   'profile_form':profile_form,
                   'registered':registered})

@login_required
def user_logout(request):
    logout(request)
    return  render(request,'app2/index.html')

def user_login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print(" failed login attempt ")
            print("Username:{} and passsword {}".format(username,password))
            return HttpResponseRedirect("invalid")

    else:
        return render(request,'app2/login.html',{})
