from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect

from .models import Blog, Category

def posts_by_category(request, category_id):
    # Fetch the posts that belong to the category with the id, category_id
    posts = Blog.objects.filter(status='Published', category=category_id)
    # Here we are using the cstegory_id bcz ForeignKey accepts only id but not names
    # use try/except when we want to do some custom action
    try:
        category = Category.objects.get(pk=category_id)
    except:
        # redirect the user to the homepage
        return redirect('home')
    # Use get_object_or_404 when you want to display 404 error page to the user
    # category = get_object_or_404(Category, pk=category_id)
    context = {
        'posts':posts,
        'category':category,
    }
    return render(request, 'posts_by_category.html', context)