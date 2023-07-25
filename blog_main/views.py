
from django.shortcuts import render

def home(request): # when home function triggers then home.html should be executed.
    return render(request, 'home.html') # render always take the request
