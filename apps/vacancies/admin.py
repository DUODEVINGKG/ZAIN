from django.contrib import admin
from apps.vacancies.models import Vacancy
from modeltranslation.admin import TranslationAdmin
# Register your models here.

class VacancyAdmin(TranslationAdmin):
    fieldsets = [
        (u'Ru', {'fields': ('title_ru', 'photo', 'description_ru',  'country_ru', 'salary_ru' )}),
        (u'En', {'fields': ('title_en',  'description_en',  'country_en', 'salary_en')})
    ]

@admin.register(Vacancy)
class VacancyModelAdmin(VacancyAdmin):
    list_display = ('title',)
    list_filter = ('title',)