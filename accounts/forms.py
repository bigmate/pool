from django import forms
class CreateUserForm(forms.Form):
    first_name = forms.CharField(max_length=50,min_length=2,widget=forms.TextInput(attrs={'class':'edge-bottom form-control','autofocus':'','placeholder':'name','required':''}))
    email = forms.EmailField(max_length=100, widget=forms.EmailInput(attrs={'class':'edge-top-bottom form-control','placeholder':'email','required':''}))
    password = forms.CharField(max_length=255,min_length=6, widget=forms.PasswordInput(attrs={'class':'edge-top form-control','placeholder':'password','required':''}))


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=100, widget=forms.EmailInput(attrs={'class':'edge-bottom form-control','placeholder':'email', 'autofocus':'','required':''}))
    password = forms.CharField(max_length=255, widget=forms.PasswordInput(attrs={'class':'edge-top form-control','placeholder':'password','required':''}))

