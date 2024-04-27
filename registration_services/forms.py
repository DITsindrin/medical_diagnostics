from django.forms import ModelForm, DateTimeInput

from medical_services.models import MedicalServices
from registration_services.models import MakeAppointment, BackCall
from services.style_form_mixin import StyleFormMixin


class BackCallForm(StyleFormMixin, ModelForm):
    """Форма обратный звонок"""

    class Meta:
        model = BackCall
        fields = ('last_name', 'phone',)


class MakeAppointmentForm(StyleFormMixin, ModelForm):
    """Форма Запись на прием для авторизованного пользователя"""

    class Meta:
        model = MakeAppointment
        fields = ('medical_services', 'date_reception',)
        widgets = {
            'date_reception': DateTimeInput(format="%Y-%m-%d %H:%M")
        }

    def __init__(self, *args, **kwargs):
        extra_param = kwargs.pop('extra_param', None)
        super(MakeAppointmentForm, self).__init__(*args, **kwargs)
        if extra_param:
            print(extra_param)
        self.fields['medical_services'].queryset = MedicalServices.objects.filter(medical_categories=extra_param)


class AnonymousMakeAppointmentForm(StyleFormMixin, ModelForm):
    """Форма Запись на прием для не авторизованного пользователя"""

    class Meta:
        model = MakeAppointment
        fields = (
            'anonymous_phone', 'anonymous_first_name', 'anonymous_last_name', 'medical_services', 'date_reception',)
        widgets = {
            'date_reception': DateTimeInput(format="%Y-%m-%d %H:%M"),
        }

    def __init__(self, *args, **kwargs):
        extra_param = kwargs.pop('extra_param', None)
        super(AnonymousMakeAppointmentForm, self).__init__(*args, **kwargs)
        if extra_param:
            print(extra_param)
        self.fields['medical_services'].queryset = MedicalServices.objects.filter(medical_categories=extra_param)
