from django.shortcuts import render,redirect
from django.contrib.auth import login
from .forms import SignUpform

# Create your views here.


def frontpage(request):
    return render(request,'core/frontpage.html')


def Signup(request):
    if request.method =='POST':
        form = SignUpform(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('frontpage')
    else:
        form = SignUpform()
    return render(request,'core/signup.html',{'form': form})