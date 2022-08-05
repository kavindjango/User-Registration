
from django.shortcuts import render,redirect
from.form import CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render (request,'home.html')


def Register(request):
    if request.method=='POST':
        name=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        
        if password1==password2:
            user=User.objects.create_user(username=name,email=email,password=password1)
            user.is_staff=True
            user.is_superuser=True
            user.save()
            messages.success(request,'your accout has been logging')
            return redirect('login')

        else:
            messages.warning(request,'password miss maching!!!')
            return redirect('Register')

    else:
        form=CreateUserForm()
        return render (request,'Register.html',{'form':form})

@login_required
def profile(request):
    return render(request,"profile.html")
