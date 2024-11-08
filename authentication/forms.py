from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


# Форма БД Логина 
class LoginForm(forms.Form):
    username = forms.CharField(max_length=15, label='Ваше имя пользователя')
    password = forms.CharField(max_length=40, widget=forms.PasswordInput, label='Ваш пароль')

# Форма БД Регистрации
class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['username', 'email','password1', 'password2']

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Пароли не совпадают.")

        if User.objects.filter(username=cleaned_data.get("username")).exists():
            raise forms.ValidationError("Пользователь с таким именем уже существует.")

        if User.objects.filter(email=cleaned_data.get("email")).exists():
            raise forms.ValidationError("Электронная почта уже зарегистрирована.")