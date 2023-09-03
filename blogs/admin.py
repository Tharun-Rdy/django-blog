from django.contrib import admin
from .models import Category, Blog, Comment

# Here we need to create class
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':  ('title',)} # Based on the title, the slug should be generated (and it is tuple we cannot add single entry, so we put a comma[,])
    list_display = ('title', 'category', 'author', 'status', 'is_featured')
    search_fields = ('id', 'title', 'category__category__name', 'status') # By using what fields you want to search the blogs
 # we want to search category field by category_name so we should use category(models)__category__name(field))
    list_editable = ('is_featured',)

admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment)
