from django import forms
from .models import post
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _


class signupform(UserCreationForm):
    password1= forms.CharField(label="Password", widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2= forms.CharField(label="Confirm Password (again)", widget=forms.PasswordInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]
        # Naming form labels
        labels = {"first_name": "First Name", "last_name":"Last Name", "email":"Email"}
        # styling form fields
        widgets = {"username":forms.TextInput(attrs={"class":"form-control"}),
        "first_name":forms.TextInput(attrs={"class":"form-control"}),
        "last_name":forms.TextInput(attrs={"class":"form-control"}),
        "email":forms.EmailInput(attrs={"class":"form-control"}), 
        }

# creating login form
class loginform(AuthenticationForm):
    #form is creating using api, no need create models
    username = UsernameField(widget=forms.TextInput(attrs={"autofocus": True, "class":"form-control"}))
    password = forms.CharField(label=_("Password"), strip= False, widget=forms.PasswordInput(attrs={"autocomplete": True, "class":"form-control"}))

class postform(forms.ModelForm):
    class Meta:
        model = post
        fields = ["title", "description"]
        labels = {"title": "Title", "description": "Description"}
        widgets = {"title": forms.TextInput(attrs={"class":"form-control"}),
                    "description": forms.Textarea(attrs={"class":"form-control"}),}
            