#CREATED FORMS FILE

from django import forms
from .models import Image

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=100, label='Username')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')

class AddUserForm(forms.Form):
    username = forms.CharField(max_length=100, label='Username')
    email = forms.CharField(max_length=50, label='Email')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
    confirm_password = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')

class PostForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea)

class EditPostForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 50}))

# class EditCommentForm(forms.Form):
#     content = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 50}))

class ImageForm(forms.ModelForm):
    class Meta:
        model=Image
        fields=("title","image",'description')

from django.contrib.auth.models import User
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    reset_profile_picture = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.HiddenInput(),
        label="Reset Profile Picture to Default"
    )

    class Meta:
        model = UserProfile
        fields = ['bio', 'location', 'profile_picture']

    widgets = {
        'profile_picture': forms.ClearableFileInput(attrs={'accept': 'image/*', 'class': 'form-control-file'}),
        'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 100, 'maxlength': '100', 'placeholder': 'Enter your bio...'}),
        'location': forms.TextInput(attrs={'class': 'form-control'}),
    }

    labels = {
        'bio': 'Biography',
        'location': 'Location',
        'profile_picture': 'Profile Picture',
    }