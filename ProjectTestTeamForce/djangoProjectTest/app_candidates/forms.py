from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ClearableFileInput
from .models import Candidate, Photo, Skill, Language


class RegisterUserForm(UserCreationForm):
    """
    Форма для регистрации пользователя
    """
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-input'}))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name')


class RegisterProfileForm(forms.ModelForm):
    """
    Форма для регистрации профиля
    """
    class Meta:
        model = Candidate
        fields = ('patronymic', 'hobbies')


class PhotoForm(forms.Form):
    """
    Форма для загрузки фотографий пользователя
    """
    image = forms.ImageField(label='Фотографии профиля', widget=ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = Photo


class SkillChoiceForm(forms.Form):
    """
    Форма для выбора или самостоятельного написания навыков
    """
    skills_1 = forms.ModelMultipleChoiceField(label='', queryset=Skill.objects.only('skill_name'), required=False)
    skills_2 = forms.CharField(label='Или впишите самостоятельно через запятую с пробелом (", ")',
                               widget=forms.TextInput(attrs={'class': 'form-input'}), required=False)

    class Meta:
        model = Skill


class LanguageChoiceForm(forms.Form):
    """
    Форма для выбора или самостоятельного написания иностранных языков
    """
    languages_1 = forms.ModelMultipleChoiceField(label='', queryset=Language.objects.only('language_name'), required=False)
    languages_2 = forms.CharField(label='Или впишите самостоятельно через запятую с пробелом (", ")',
                                  widget=forms.TextInput(attrs={'class': 'form-input'}), required=False)

    class Meta:
        model = Language