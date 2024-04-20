from django.shortcuts import render
from django.views.generic import ListView, DetailView

from medical_services.models import MedicalCategories
from information.models import Information


# Create your views here.
def index(request):
    """Вывод главной страницы"""
    title = 'Сеть медицинских центров «СМ-Клиника»'
    mission = 'Здоровье – самый ценный ресурс. Вернуть его, сохранить, преумножить!'
    information = Information.objects.all()
    context = {
        'title': title,
        'mission': mission,
        'information': information
    }
    return render(request, 'medical_services/info_index.html', context)


class MedicalCategoriesListView(ListView):
    """Вывод категорий диагности"""

    model = MedicalCategories
    paginate_by = 8

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Диагностика'

        return context


class MedicalCategoriesDetailView(DetailView):
    """Вывод подробной информации о настройки рассылки"""
    model = MedicalCategories

    def get(self, request, *args, **kwargs):
        object = self.get_object()
        medical_services = object.medicalservices_set.all()
        doctors = object.medicalstaff_set.all()

        context = {
            'object': object,
            'medical_services': medical_services,
            'doctors': doctors,
        }

        return render(request, 'medical_services/medicalcategories_detail.html', context)
