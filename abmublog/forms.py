from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *

class CreateUserForm(UserCreationForm):
    email=forms.EmailField(required='required')
    first_name=forms.CharField(max_length=100)
    last_name=forms.CharField(max_length=100)
    class Meta:
        model=User
        fields=['first_name','last_name','username','email','password1','password2']
        widgets={
              'frist_name': forms.TextInput(attrs={'class': 'form-control',}),
            'last_name': forms.TextInput(attrs={'class': 'form-control',}),
            'username':forms.TextInput(),
            'email':forms.EmailInput(),
            'password1':forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}),
            'password2':forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm Password'}),
        }
        help_texts = {
            'password1': "* Your password must contain at least 8 characters.",
            'password2': "* Your password can’t be entirely numeric.",
        }
class Orderform(forms.ModelForm):
    class Meta:
        model=Order
        fields = ['name', 'type', 'title', 'status']
        widgets = {
            'name': forms.TextInput(attrs={'type': 'hidden'}),
            'type': forms.Select(attrs={'class': 'form-control'},),
            'title': forms.TextInput(attrs={'class': 'form-control'},),
            'status': forms.TextInput(attrs={'type': 'hidden'}),
            }
class MakeOrderForm(forms.ModelForm):
    class Meta:
        model=MakeOrder
        fields = ['author', 'type', 'title', 'image']
        widgets = {
            'author': forms.TextInput(attrs={'type': 'hidden'}),
            'type': forms.Select(attrs={'class': 'form-control'}, ),
            'title': forms.TextInput(attrs={'class': 'form-control'}, ),

        }
class EditMakeOrderForm(forms.ModelForm):
    class Meta:
        model=MakeOrder
        fields = ['author', 'type', 'title', 'image']
        widgets = {
            'author': forms.TextInput(attrs={'type': 'hidden'}),
            'type': forms.Select(attrs={'class': 'form-control'}, ),
            'title': forms.TextInput(attrs={'class': 'form-control'}, ),

        }

class OrderUpdateForm(forms.ModelForm):
    class Meta:
        model=Order
        fields=['status']
        widgets = {
            'status': forms.Select(attrs={'class': 'form-control'}, ),
        }
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', }),
            'last_name': forms.TextInput(attrs={'class': 'form-control', }),
            'username': forms.TextInput(attrs={'class': 'form-control', }),
             'email':forms.EmailInput(attrs={'class':'form-control'}),
        }
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['address','phone','gender','image']
        widgets = {
            'address': forms.TextInput(attrs={'class': 'form-control', }),
            'phone': forms.TextInput(attrs={'class': 'form-control', }),
            'gender': forms.Select(attrs={'class': 'form-control', }),

        }
class AddProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields='__all__'

class SuggestForm(forms.ModelForm):
    class Meta:
        model=Suggestion
        fields=['user','suggestion']
        widgets = {
              'user':forms.TextInput(attrs={'type':'hidden'}),
             'suggestion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'your suggestion here!',})
        }
