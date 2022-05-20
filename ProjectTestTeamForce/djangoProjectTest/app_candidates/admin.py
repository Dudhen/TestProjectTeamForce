from django.contrib import admin
from .models import Candidate, Skill, Language


class CandidateAdmin(admin.ModelAdmin):
    """Класс для работы с моделью кандидата в админ-панели"""
    list_display = ['name', 'surname', 'patronymic', 'hobbies', 'created_at']
    list_display_links = ['name']
    list_filter = ['created_at']


class SkillAdmin(admin.ModelAdmin):
    """Класс для работы с моделью навыка в админ-панели"""
    list_display = ['skill_name']
    list_display_links = ['skill_name']


class LanguageAdmin(admin.ModelAdmin):
    """Класс для работы с моделью языка в админ-панели"""
    list_display = ['language_name']
    list_display_links = ['language_name']


admin.site.register(Candidate, CandidateAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Language, LanguageAdmin)