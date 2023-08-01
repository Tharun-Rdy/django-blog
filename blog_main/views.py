from django.shortcuts import render, redirect
from blogs.models import Blog, Category
from assignments.models import About
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth

def home(request): # when home function triggers then home.html should be executed.
    categories = Category.objects.all()
    featured_posts = Blog.objects.filter(is_featured=True, status='Published').order_by('-updated_at') # we are using filter bcz we want to add a condition to this query
    posts = Blog.objects.filter(is_featured=False, status='Published' )
    # If post is Drafted or not published then we are not supposed to display it to the user.
    # Fetch about us
    try:
        about = About.objects.get()
    except:
        about = None
    context = {   # we will send the categories to home.html
        'featured_posts': featured_posts,
        'posts': posts,
        'about': about,
    }
    # print statement is used when we want to see the output in the terminal
    return render(request, 'home.html', context) # render always take the request


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
    else:
        form = RegistrationForm()
    context = {
        'form': form,
    }
    return render(request, 'register.html', context)

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
            return redirect('dashboard')
    form = AuthenticationForm()
    context = {
        'form':form,
    }
    return render(request, 'login.html', context)

def logout(request):
    auth.logout(request)
    return redirect('home')