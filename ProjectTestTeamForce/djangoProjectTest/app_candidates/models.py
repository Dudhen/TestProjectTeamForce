from django.db import models
from django.contrib.auth.models import User


class Skill(models.Model):
    """
    Модель навыка
    """
    skill_name = models.CharField(max_length=50, blank=False, verbose_name='Название навыка')

    def __str__(self):
        return str(self.skill_name)

    class Meta:
        verbose_name_plural = 'навыки'
        verbose_name = 'навык'


class Language(models.Model):
    """
    Модель языка
    """
    language_name = models.CharField(max_length=50, blank=False, verbose_name='Название языка')

    def __str__(self):
        return str(self.language_name)

    class Meta:
        verbose_name_plural = 'языки'
        verbose_name = 'язык'


class Candidate(models.Model):
    """
    Модель кандидата (профиля)
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    USERNAME_FIELD = 'user'
    name = models.CharField(max_length=36, blank=False, verbose_name='Имя')
    surname = models.CharField(max_length=36, blank=False, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=36, blank=True, verbose_name='Отчество')
    skills = models.ManyToManyField(Skill)
    languages = models.ManyToManyField(Language)
    hobbies = models.CharField(max_length=1000, blank=True, verbose_name='Увлечения')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name_plural = 'кандидаты'
        verbose_name = 'кандидат'


class Photo(models.Model):
    """
    Модель фотографии кандидата (пользователя)
    """
    image = models.ImageField(upload_to='photos/', blank=True, verbose_name='Фото')
    candidate = models.ForeignKey(Candidate, null=True, default=None, on_delete=models.CASCADE,
                                  related_name='photos', verbose_name='Кандидат')

    class Meta:
        verbose_name_plural = 'фотографии'
        verbose_name = 'фотография'