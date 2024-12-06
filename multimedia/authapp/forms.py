from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text="Optional")
    last_name = forms.CharField(max_length=30, required=False, help_text="optional")
    email = forms.EmailField(max_length=254, help_text= "Enter a valid email address ")
    
    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2"
        ]

class User_form(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]
class UserProfile_form(forms.ModelForm):
    gend = [
        ("Male", "Male"),
        ("Female", "Female"),
    ]
    Country = [
        ("Nigeria", "Nigeria"),
        ("Ghana", "Ghana"),
        ("Kenya", "Kenya"),
        ("Ugnadan", "Ugandan"),
        ("South Africa", "South Africa")
    ]
    
    profile_picture = forms.ImageField(required=False, label= "Display Picture")
    gender = forms.ChoiceField(choices= gend, required= False, widget=forms.RadioSelect)
    country =forms.ChoiceField(choices=Country, required=False)
    
    class Meta:
        model = UserProfile
        fields = [
            "profile_picture",
            "sex",
            "country",
        ]
    