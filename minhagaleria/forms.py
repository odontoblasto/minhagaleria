from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import ProfileModel,PhotoModel


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Enter username...'})
        self.fields['password1'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Enter password...'})
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Confirm password...'})

class ProfilePageForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ('user_name','data_nascimento','foto',)
        widget ={
                'user_name':forms.TextInput(attrs={'class':'form-control'}),
                'data_nascimento':forms.DateInput(attrs={'class':'form-control'}),
                #'detalhes':forms.TextInput(attrs={'class':'form-control'})
                }

class AddPhotoGamesForm(forms.ModelForm):
    class Meta:
        model = PhotoModel
        fields = ('category_name','image','description',)
        widget = {
                #'category_name':forms.TextInput(attrs={'class':'form-control'}),
                'description':forms.TextInput(attrs={'class':'form-control'}),
                #'detalhes':forms.TextInput(attrs={'class':'form-control'})
                }