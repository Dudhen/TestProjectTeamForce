from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from ..models import Candidate


class RegisterPageTest(TestCase):
    """Класс для тестов страницы регистрации"""

    def test_register_page(self):
        """Тест правильной загрузки страницы регистрации и использование правильного шаблона"""
        url = reverse('registration')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'candidates/registration.html')


class LoginPageTest(TestCase):
    """Класс для тестов страницы входа"""

    def test_login_page(self):
        """Тест правильной загрузки страницы входа и использование правильного шаблона"""
        url = reverse('login')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'candidates/login.html')


class CandidateListPageTest(TestCase):
    """Класс для тестов страницы списка кандидатов"""

    def test_candidate_list_page(self):
        """Тест правильной загрузки страницы списка кандидатов и использование правильного шаблона"""
        url = reverse('candidates')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'candidates/candidate_list.html')


class CandidateDetailPageTest(TestCase):
    """Класс для тестов страницы детальной страницы кандидата"""

    def setUp(self):
        """Создание пользователя"""
        self.user = User.objects.create(username='test_user',
                                        is_superuser=False,
                                        is_staff=False,
                                        is_active=True)
        self.user.set_password('random123')
        self.user.save()

    def test_candidate_detail_page(self):
        """Тест правильной загрузки детальной страницы кандидата и использование правильного шаблона"""
        candidate = Candidate.objects.create(name='random_name',
                                             user=self.user,
                                             surname='random_surname',
                                             patronymic='random_patronymic')
        candidate.save()
        url = reverse('candidate-detail', kwargs={'pk': candidate.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'candidates/candidate_detail.html')


class ProfileDetailPageTest(TestCase):
    """Класс для тестов страницы личного кабинета пользователя"""

    def setUp(self):
        """Создание пользователя"""
        self.user = User.objects.create(username='test_user',
                                        is_superuser=False,
                                        is_staff=False,
                                        is_active=True)
        self.user.set_password('random123')
        self.user.save()

    def test_profile_detail_page(self):
        """Тест правильной загрузки страницы личного кабинета и использование правильного шаблона"""
        candidate = Candidate.objects.create(name='random_name',
                                             user=self.user,
                                             surname='random_surname',
                                             patronymic='random_patronymic')
        candidate.save()
        self.client.login(username='test_user', password='random123')
        url = reverse('profile')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'candidates/profile_detail.html')


class ProfileSkillAddPageTest(TestCase):
    """Класс для тестов страницы добавления новых навыков пользователя"""

    def setUp(self):
        """Создание пользователя"""
        self.user = User.objects.create(username='test_user',
                                        is_superuser=False,
                                        is_staff=False,
                                        is_active=True)
        self.user.set_password('random123')
        self.user.save()

    def test_profile_skill_add_page(self):
        """
        Тест правильной загрузки страницы добавления новых навыков пользователя и использование правильного шаблона
        """
        candidate = Candidate.objects.create(name='random_name',
                                             user=self.user,
                                             surname='random_surname',
                                             patronymic='random_patronymic')
        candidate.save()
        self.client.login(username='test_user', password='random123')
        url = reverse('profile-skill-add')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'candidates/profile_skill_add.html')


class ProfileLanguageAddPageTest(TestCase):
    """Класс для тестов страницы добавления новых языков пользователя"""

    def setUp(self):
        """Создание пользователя"""
        self.user = User.objects.create(username='test_user',
                                        is_superuser=False,
                                        is_staff=False,
                                        is_active=True)
        self.user.set_password('random123')
        self.user.save()

    def test_profile_language_add_page(self):
        """
        Тест правильной загрузки страницы добавления новых языков пользователя и использование правильного шаблона
        """
        candidate = Candidate.objects.create(name='random_name',
                                             user=self.user,
                                             surname='random_surname',
                                             patronymic='random_patronymic')
        candidate.save()
        self.client.login(username='test_user', password='random123')
        url = reverse('profile-language-add')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'candidates/profile_language_add.html')