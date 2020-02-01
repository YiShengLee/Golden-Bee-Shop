from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import auth, messages
from .forms import UserLoginForm
from django.contrib.auth.decorators import login_required

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

@login_required
def profile(request):
    return render(request, 'user_profile.template.html')