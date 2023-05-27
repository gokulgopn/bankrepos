from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
# Create your views here.
def home(request):
    return render(request,'home.html')
def loginn(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password = request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('new')
        # else:
        #     return HttpResponse("username or Password is incorrect")
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')

        # if password1!=password2:
        #     return HttpResponse("Password incorrect")
        # else:
        my_user=User.objects.create_user(username,password1)
        my_user.save()
        return redirect('loginn')

    return render(request, 'register.html')

def new(request):
    return render(request, 'new.html')

def form(request):
    return render(request, 'form.html')

def final(request):
    return render(request, 'final.html')

def redirect_idukki(request):
    return redirect("https://en.wikipedia.org/wiki/Idukki_district")
def redirect_kottayam(request):
    return redirect("https://en.wikipedia.org/wiki/Kottayam")
def redirect_malappuram(request):
    return redirect("https://en.wikipedia.org/wiki/Malappuram")
def redirect_palakkad(request):
    return redirect("https://en.wikipedia.org/wiki/Palakkad")
def redirect_kochi(request):
    return redirect("https://en.wikipedia.org/wiki/Kochi")
