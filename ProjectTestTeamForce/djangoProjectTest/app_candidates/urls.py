from django.urls import path
from .views import CandidateListView, CandidateDetailView, UserLoginView, UserLogout, UserRegister, \
    ProfileSkillAddFormView, ProfileDetailView, ProfileLanguageAddFormView

"""URL-ы проекта"""
urlpatterns = [
    path(r'candidates/', CandidateListView.as_view(), name='candidates'),
    path(r'candidates/<int:pk>/', CandidateDetailView.as_view(), name='candidate-detail'),
    path(r'login/', UserLoginView.as_view(), name='login'),
    path(r'logout/', UserLogout.as_view(), name='logout'),
    path(r'registration/', UserRegister.as_view(), name='registration'),
    path(r'profile/', ProfileDetailView.as_view(), name='profile'),
    path(r'profile/skill_add/', ProfileSkillAddFormView.as_view(), name='profile-skill-add'),
    path(r'profile/language_add/', ProfileLanguageAddFormView.as_view(), name='profile-language-add'),
]