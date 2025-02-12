from django.contrib import admin
from apps.base.models  import Base
from apps.contacts.models import Contact
from apps.base.models  import Base, Banner, Counter, Reviews,File
from django.contrib.auth.models import User, Group
from django.contrib import messages
from modeltranslation.admin import TranslationAdmin

# class BannerGlAdmin(admin.ModelAdmin):
#     def has_add_permission(self, request):
#         return not Banner.objects.exists()

#     def save_model(self, request, obj, form, change):
#         if Banner.objects.exists() and not change:
#             self.message_user(
#                 request,
#                 'Вы не можете добавлять более 1 баннера, вы можете только изменять существующий баннер.',
#                 level=messages.ERROR
#             )
#             return 
#         super().save_model(request, obj, form, change)

class BannerAdmin(TranslationAdmin):  
    fieldsets = [
        (u'Ru', {'fields': ('title_ru', 'photo', 'photo2')}),
        (u'En', {'fields': ('title_en',)})
    ]

@admin.register(Banner)
class BannerModelAdmin(BannerAdmin):
    list_display = ('title',)
    list_filter = ('title',)

admin.site.register(Counter)

class BaseAdmin(TranslationAdmin):  
    fieldsets = [
        (u'Ru', {'fields': ('address_ru', 'email', 'phone','instagram','whatsapp','telegram',)}),
        (u'En', {'fields': ('address_en',)})
    ]

@admin.register(Base)
class BaseModelAdmin(BaseAdmin):
    list_display = ('address',)
    list_filter = ('address',)

admin.site.register(Contact)

class ReviewAdmin(TranslationAdmin):
    fieldsets = [
        (u'Ru', {'fields': ('name_ru','description_ru','photo'  )}),
        (u'En', {'fields': ('name_en',  'description_en')})
    ]

@admin.register(Reviews)
class ReviewModelAdmin(ReviewAdmin):
    list_display = ('name',)
    list_filter = ('name',)


admin.site.unregister(User)
admin.site.unregister(Group)

admin.site.register(File)