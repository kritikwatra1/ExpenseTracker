from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField()


class SignupForm(forms.Form):
    Emailid = forms.EmailField()
    Password = forms.CharField()
    Firstname = forms.CharField()
    Lastname = forms.CharField()
