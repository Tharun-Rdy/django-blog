from django.contrib import admin
from .models import About, SocialLink


class AboutAdmin(admin.ModelAdmin):# i.e., we are taking all the ModelAdmin features inside the AboutAdmin class
    def has_add_permission(self, request):  # This function is responsible for giving the permission to model for adding any data in the admin panel
        count = About.objects.all().count()
        if count == 0:
            return True
        else:
            return False

admin.site.register(About, AboutAdmin)
admin.site.register(SocialLink)