from django.shortcuts import render

from information.models import Contacts, Information


# Create your views here.

def contacts(request):
    """Контроллер страницы с контактами"""
    contact = Contacts.objects.all()
    title = 'Наши контакты'
    context = {
        'contact': contact,
        'title': title,
    }

    return render(request, 'information/contacts.html', context)
