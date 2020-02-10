from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import auth, messages
from .forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import MyUser
from django.core.mail import BadHeaderError, send_mail

# Create your views here.
def members(request):
    return render(request, 'members.template.html')

def login(request):
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)
        username = request.POST['username']
        password=request.POST['password']
        user = auth.authenticate(username=username, password=password)
        
        # User is return by auth.authenticate
        if user:
            # Log in the user account
            auth.login(user=user, request=request)
            messages.success(request, "You have successfully logged in")
            return redirect(reverse('show_products'))
        
        # If user is not valid
        else:
            login_form.add_error(None,"Invalid username or password")
            return render(request, 'login.template.html', {
              'form':login_form
            })
    
    else:
        login_form = UserLoginForm()
        return render(request, 'login.template.html',{
            'form':login_form
        })

def logout(request):
    auth.logout(request)
    messages.success(request, "You have successfully been logged out")
    return redirect(reverse('members'))  

def register(request):
    User = get_user_model()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # Create the user from the form
            form.save()
            # Check if the user has been created properly
            user = auth.authenticate(username=request.POST['username'],
                                    password=request.POST['password1'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully registered")
            else:
                messages.error(request, "Unable to register your account at this time")
            return redirect(reverse('index'))
        else:
            return render(request, 'register.template.html',{
                'form':form
            })
    else:
        form = UserRegistrationForm()
        return render(request, 'register.template.html',{
            'form':form
        })


@login_required
def profile(request):
    return render(request, 'user_profile.template.html')