from django.shortcuts import render
from blogs.models import Blog, Category

def home(request): # when home function triggers then home.html should be executed.
    categories = Category.objects.all()
    featured_posts = Blog.objects.filter(is_featured=True, status='Published').order_by('-updated_at') # we are using filter bcz we want to add a condition to this query
    posts = Blog.objects.filter(is_featured=False, status='Published' )
    # If post is Drafted or not published then we are not supposed to display it to the user.
    
    context = {   # we will send the categories to home.html
        'featured_posts': featured_posts,
        'posts': posts,
    }
    # print statement is used when we want to see the output in the terminal
    return render(request, 'home.html', context) # render always take the request
