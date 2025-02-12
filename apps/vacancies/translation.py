from modeltranslation.translator import translator, TranslationOptions
from apps.vacancies.models import Vacancy

class VacancyTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'country', 'salary')


translator.register(Vacancy, VacancyTranslationOptions)