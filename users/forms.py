from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models


# class CreateProfile(forms.ModelForm):
#     class Meta():
#         model = models.Profile
#         fields = []

class CreateProfile(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None


# class Follow_form(forms.ModelForm):
#     class Meta():
#         model = models.Follow
#         fields = []
