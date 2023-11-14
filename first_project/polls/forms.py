from django import forms


# class NameForm(forms.Form):
#     your_name = forms.CharField(label="Your name", max_length=100)

#https://docs.djangoproject.com/en/4.2/topics/forms/

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=100, label='Username')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')

class AddUserForm(forms.Form):
    username = forms.CharField(max_length=100, label='Username')
    email = forms.CharField(max_length=50, label='Email')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
    confirm_password = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')
    