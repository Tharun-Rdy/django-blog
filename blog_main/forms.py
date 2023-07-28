from django.contrib.auth.models import User  # User model is the default user model created by django itself
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2')
# UserCreationForm is responsible for rendering the users default form in the admin site