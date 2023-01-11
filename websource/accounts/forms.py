from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import TextInput, PasswordInput, CharField, EmailField, EmailInput


class RegisterUserForm(UserCreationForm):
    username = CharField(label='Логиин', widget=TextInput(attrs={'class': 'form-input'})),
    email = EmailField(label='Email', widget=EmailInput(attrs={'class': 'form-input'})),
    password1 = CharField(label='Пароль', widget=PasswordInput(attrs={'class': 'form-input'})),
    password2 = CharField(label='Повтор пароля', widget=PasswordInput(attrs={'class': 'form-input'})),
    first_name = CharField(label='Имя', widget=TextInput(attrs={'class': 'form-input'})),
    last_name = CharField(label='Фамилия', widget=TextInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name')
        # widges = {
        #     'username': TextInput(attrs={'class': 'form-input'}),
        #     'password1': PasswordInput(attrs={'class': 'form-input'}),
        #     'password2': PasswordInput(attrs={'class': 'form-input'}),
        #     'first_name': TextInput(attrs={'class': 'form-input'}),
        #     'last_name': TextInput(attrs={'class': 'form-input'})
        # }