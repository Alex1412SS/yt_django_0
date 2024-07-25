from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import profile_model

class New_user_form(UserCreationForm):
    email = forms.EmailField(required=True)
    username = forms.CharField(required=True)
    password1 = forms.CharField(required=True)
    password2 = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", 'password1', 'password2')


    # def save(self, commit=True):
    #     user = super(New_user_form, self).save(commit=False)
    #     user.email = self.cleaned_data['email']
    #     if commit:
    #         user.save()
    #     return user

class profile(forms.ModelForm):
    class Meta:
        user = User
        model = profile_model
        fields = ('image', 'user',)