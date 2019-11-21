from django import forms
from django.contrib.auth import get_user_model


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = get_user_model()
        fields = ('username', 'password', 'email')
        error_messages = {
            'username':
                {'unique': 'Пользователь с данным именем уже существует'},
            'email':
                {'unique': 'Пользователь с данным почтовым адресом уже существует'},
        }

