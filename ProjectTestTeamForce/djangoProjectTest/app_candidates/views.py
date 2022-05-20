from django.core.files.base import ContentFile
from django.urls import reverse_lazy
from .models import Candidate, Skill, Language, Photo
from django.views import generic
from django.views.generic.edit import CreateView, FormView
from .forms import RegisterUserForm, RegisterProfileForm, PhotoForm, SkillChoiceForm, LanguageChoiceForm
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView


class CandidateListView(generic.ListView):
    """Представление для страницы со списком кандидатов"""
    model = Candidate
    template_name = 'candidates/candidate_list.html'

    def get_queryset(self):
        """Метод для отображения кандидатов по дате регистрации (сначала новые)"""
        return Candidate.objects.order_by('-created_at')


class CandidateDetailView(generic.DetailView):
    """Представление для детальной страницы кандидата"""
    model = Candidate
    template_name = 'candidates/candidate_detail.html'

    def get_context_data(self, **kwargs):
        """Метод для отображения фотографий кандидата"""
        context = super(CandidateDetailView, self).get_context_data(**kwargs)
        context['photos'] = self.object.photos.select_related('candidate')
        return context


class UserLoginView(LoginView):
    """Представление для страницы входа"""
    template_name = 'candidates/login.html'


class UserLogout(LogoutView):
    """Представление для страницы выхода и перенаправления на страницу входа"""
    next_page = '/login/'


class UserRegister(CreateView):
    """Представление для страницы регистрации"""
    form_class = RegisterUserForm
    form_class_profile = RegisterProfileForm
    form_class_skills = SkillChoiceForm
    form_class_languages = LanguageChoiceForm
    form_class_photos = PhotoForm
    template_name = 'candidates/registration.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        """Метод для отображения форм для заполнения"""
        context = super(UserRegister, self).get_context_data(**kwargs)
        context['user_form'] = self.form_class
        context['profile_form'] = self.form_class_profile
        context['skills_form'] = self.form_class_skills
        context['language_form'] = self.form_class_languages
        context['photo_form'] = self.form_class_photos
        return context

    def post(self, request, *args, **kwargs):
        """Метод для получения данных с заполненных форм"""
        user_form = RegisterUserForm(request.POST)
        profile_form = RegisterProfileForm(request.POST)
        skills_form = SkillChoiceForm(request.POST)
        language_form = LanguageChoiceForm(request.POST)
        photo_form = RegisterProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid()\
                and skills_form.is_valid() and language_form.is_valid() and photo_form.is_valid():
            user = user_form.save(commit=False)
            profile = profile_form.save(commit=False)
            skills = [Skill.objects.get(skill_name=i_name) for i_name in skills_form.cleaned_data['skills_1']]
            for i_skill in skills_form.cleaned_data['skills_2'].split(', '):
                skill = Skill.objects.get_or_create(skill_name=i_skill)
                skills.append(skill[0])
            languages = [Language.objects.get(language_name=i_name) for i_name in language_form.cleaned_data['languages_1']]
            for i_language in language_form.cleaned_data['languages_2'].split(', '):
                language = Language.objects.get_or_create(language_name=i_language)
                languages.append(language[0])
            user.save()
            profile.name = user.first_name
            profile.surname = user.last_name
            profile.user = user
            profile.save()
            profile.skills.set(skills)
            profile.languages.set(languages)
            for f in request.FILES.getlist('image'):
                data = f.read()
                photo = Photo(candidate=profile)
                photo.image.save(f.name, ContentFile(data))
                photo.save()
            return redirect('login')
        else:
            return render(request, self.template_name, {'user_form': user_form, 'profile_form': profile_form,
                                                        'skills_form': skills_form, 'language_form': language_form,
                                                        'photo_form': photo_form})


class ProfileDetailView(generic.ListView):
    """Представление для страницы личного кабинета пользователя"""
    model = Candidate
    template_name = 'candidates/profile_detail.html'

    def get_context_data(self, **kwargs):
        """Метод для отображения данных пользователя"""
        context = super(ProfileDetailView, self).get_context_data(**kwargs)
        context['object'] = Candidate.objects.all().filter(id=self.request.user.candidate.id)[0]
        return context


class ProfileSkillAddFormView(FormView):
    """Представление для страницы добавления навыков пользователя"""
    form_class = SkillChoiceForm
    template_name = 'candidates/profile_skill_add.html'
    success_url = reverse_lazy('profile')

    def post(self, request, *args, **kwargs):
        """Метод для получения данных с заполненных форм навыков"""
        skills_form = SkillChoiceForm(request.POST)
        if skills_form.is_valid():
            skills = [Skill.objects.get(skill_name=i_name) for i_name in skills_form.cleaned_data['skills_1']]
            for i_skill in skills_form.cleaned_data['skills_2'].split(', '):
                skill = Skill.objects.get_or_create(skill_name=i_skill)
                skills.append(skill[0])
            [self.request.user.candidate.skills.add(i_skill) for i_skill in skills]
            return redirect('profile')
        else:
            return render(request, self.template_name, {'skills_form': skills_form})


class ProfileLanguageAddFormView(FormView):
    """Представление для страницы добавления языков пользователя"""
    form_class = LanguageChoiceForm
    template_name = 'candidates/profile_language_add.html'
    success_url = reverse_lazy('profile')

    def post(self, request, *args, **kwargs):
        """Метод для получения данных с заполненных форм языков"""
        language_form = LanguageChoiceForm(request.POST)
        if language_form.is_valid():
            languages = [Language.objects.get(language_name=i_name) for i_name in language_form.cleaned_data['languages_1']]
            for i_language in language_form.cleaned_data['languages_2'].split(', '):
                language = Language.objects.get_or_create(language_name=i_language)
                languages.append(language[0])
            [self.request.user.candidate.languages.add(i_language) for i_language in languages]
            return redirect('profile')
        else:
            return render(request, self.template_name, {'language_form': language_form})