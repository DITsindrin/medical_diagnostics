import re

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from registration_services.forms import MakeAppointmentForm, AnonymousMakeAppointmentForm, BackCallForm
from registration_services.models import MakeAppointment, BackCall
from users.models import MedicalStaff


# Create your views here.

def success_message(request):
    """Сообщение об успешной регистрации или о обратном звонке для неавторизованного пользователя"""
    return render(request, 'registration_services/success_message.html')


def success_message_call(request):
    """Сообщение об успешной регистрации или о обратном звонке для неавторизованного пользователя"""
    return render(request, 'registration_services/success_message_call.html')


class BackCallCreateView(CreateView):
    model = BackCall
    form_class = BackCallForm
    success_url = reverse_lazy('registration_services:success_message_call')


class MakeAppointmentCreateView(CreateView):
    """Регистрации записи на прием к врачу"""

    model = MakeAppointment
    success_url = reverse_lazy('registration_services:success_message')
    form_class = MakeAppointmentForm

    def get_form_kwargs(self):
        url = self.request.path
        id_pk = re.findall(r'\b\d+\b', url)
        doctor = MedicalStaff.objects.get(pk=id_pk[0])
        medical_categories_id = doctor.medical_category.id
        kwargs = super().get_form_kwargs()
        kwargs['extra_param'] = medical_categories_id  # Добавляем ваш параметр
        return kwargs

    def get_form_class(self):
        if not self.request.user.is_authenticated:
            form_class = AnonymousMakeAppointmentForm

            return form_class

        return self.form_class

    def form_valid(self, form):
        url = self.request.path
        id_pk = re.findall(r'\b\d+\b', url)
        doctor = MedicalStaff.objects.get(pk=id_pk[0])
        form.instance.patient = self.request.user
        form.instance.doctor = doctor

        return super().form_valid(form)


class MakeAppointmentListView(LoginRequiredMixin, ListView):
    """Вывод всех записей на прием к врачу"""

    model = MakeAppointment
    paginate_by = 8

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Ваши записи'

        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        current_user = self.request.user
        queryset = queryset.filter(patient=current_user).filter()

        return queryset
