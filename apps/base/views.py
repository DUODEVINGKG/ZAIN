from django.shortcuts import render, get_object_or_404
from apps.base.models import Base, Banner, Counter, Reviews,File
from apps.contacts.models import Contact
from apps.telegram_bot.views import get_text
from apps.vacancies.models import Vacancy
from django.utils.translation import get_language
from django.urls import exceptions

def get_common_context():
    title = Banner.objects.latest('id')
    base = Base.objects.latest('id')
    counter = Counter.objects.latest('id')
    reviews = Reviews.objects.all()
    vacancy = Vacancy.objects.all()
    file = File.objects.latest('id')
    current_language = get_language() 
    return {
        'base': base,
        'title': title,
        'counter': counter,
        'reviews': reviews,
        'vacancy': vacancy,
        'file': file,
        'current_language': current_language, 
    }

def index(request):
    context = get_common_context()
    return render(request, 'base/index.html', context)

def project_details(request, id):
    context = get_common_context()
    vacancy = get_object_or_404(Vacancy, id=id)
    context['vacancy'] = vacancy
    return render(request, 'base/project-details.html', context)

def contact(request):
    context = get_common_context()
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact = Contact.objects.create(name=name, email=email, phone=phone, subject=subject, message=message)
        get_text(f"""
    отправлен запрос на обратную связь 
                    
    Имя {name}
    Почта {email}
    Номер телефона {phone}
    Объект {subject}
    Сообщение {message}
    """)
    return render(request, 'base/contact.html', context)


def error(request,exception=None):
    context = get_common_context()
    return render(request, 'error/error.html', status=404)


from urllib.parse import urlparse
from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls.base import resolve, reverse
from django.urls.exceptions import Resolver404
from django.utils import translation


def set_language(request, language):
    for lang, _ in settings.LANGUAGES:
        translation.activate(lang)
        try:
            view = resolve(urlparse(request.META.get("HTTP_REFERER")).path)
        except Resolver404:
            view = None
        if view:
            break
    if view:
        translation.activate(language)
        next_url = reverse(view.url_name, args=view.args, kwargs=view.kwargs)
        response = HttpResponseRedirect(next_url)
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    else:
        response = HttpResponseRedirect("/")
    return response