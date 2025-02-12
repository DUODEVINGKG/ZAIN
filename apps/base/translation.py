from modeltranslation.translator import translator, TranslationOptions
from apps.base.models import Banner,Base,Reviews

class BannerTranslationOptions(TranslationOptions):
    fields = ('title',)


translator.register(Banner, BannerTranslationOptions)

class BaseTranslationOptions(TranslationOptions):
    fields = ('address',)


translator.register(Base, BaseTranslationOptions)



class ReviewsTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)

translator.register(Reviews, ReviewsTranslationOptions)

