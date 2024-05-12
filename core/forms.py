from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ('username', 'email','password1','password2')

    username = forms.CharField(
        widget=forms.TextInput(attrs={ 
                               'placeholder':'your name',
                               'class':'w-full py-4 px-6 rounded-xl'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={ 
                               'placeholder':'your email address',
                               'class':'w-full py-4 px-6 rounded-xl'})
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={ 
                               'placeholder':'your password',
                               'class':'w-full py-4 px-6 rounded-xl'})
    )
    
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={ 
                               'placeholder':'Confirm password',
                               'class':'w-full py-4 px-6 rounded-xl'})
    )
