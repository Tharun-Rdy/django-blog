from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True) # once a category is created with a name then that name should not be re-used.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'categories'

    # Here we are setting a string representation of the category model
    def __str__(self): # whenever you write any member function inside the class - you should always pass self as a parameter
        return self.category_name
    
    # creating a drop down 
STATUS_CHOICES = (
    ("Draft", "Draft"),
    ("Published", "Published")
)
    
class Blog(models.Model):
    title = models.CharField(max_length=100)
    slug =  models.SlugField(max_length=150, unique=True, blank=True)  # slug is a part of url that identifies a particular page on our website and it is very useful in SEO. (i.e it is more similar like title with hyphens '-' in b/w instead of spaces [kebab case])
    category = models.ForeignKey(Category, on_delete = models.CASCADE) # When we delete the specific category the blog post assoc. with that category should also be deleted.
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    featured_image = models.ImageField(upload_to='uploads/%Y/%m/%d') # It will create a folder with the name of current year,month,date
      # for featured_image we need to install pillow in the terminal
    short_description = models.TextField(max_length=500)
    blog_body = models.TextField(max_length=2000)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Draft")     # status will be drop down bcz status should be either draft or published
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # we can add string representation of the model for this model.
    def __str__(self):
        return self.title    
    
class Comment(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
        comment = models.TextField(max_length=250)
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)

        def  __str__(self):
            return self.comment