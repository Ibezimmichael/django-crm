from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Customer
from django import forms
from django.forms.widgets import PasswordInput, TextInput

# register form

class RegisterForm(UserCreationForm):
    
    class Meta:        
        model = User
        fields = ['username', 'password1', 'password2']
        
        
# login form

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())
    
    
# - Create a record

class CreateCustomerForm(forms.ModelForm):
    class Meta:

        model = Customer
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'city', 'state', 'country']
        
class UpdateCustomerForm(forms.ModelForm):
    class Meta:

        model = Customer
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'city', 'state', 'country']
        




















