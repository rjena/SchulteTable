from django import forms

from .models import UserST

class SignupForm(forms.ModelForm):

    class Meta:
        model = UserST
        fields = ('login', 'email', 'name', 'bday', 'password',)
