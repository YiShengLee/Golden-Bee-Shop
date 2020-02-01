from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import auth, messages

# Create your views here.
def members(request):
    return render(request, 'members.template.html')

def logout(request):
    auth.logout(request)
    messages.success(request, "You have successfully been logged out")
    return redirect(reverse('members'))    