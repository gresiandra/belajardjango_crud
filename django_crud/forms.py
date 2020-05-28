from django import forms
from django.contrib.auth.models import User

class loginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "username",
            "password",
        ]
        labels = {
            "username": "Username",
            "password": "Password"
        }
    
        widgets = {
            'username': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Isi Username',
                    'required': True
                }
            ),

            'password': forms.PasswordInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Isi Password',
                    'required': True
                }
            )

        }
