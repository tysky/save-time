from django import forms
from .models import Frog, Task


class DateTypeInput(forms.DateInput):
    input_type = 'date'


class ChooseDateForm(forms.Form):
    date_form = forms.DateField(label='Choose date', widget=DateTypeInput())


# class SetFrogForm(forms.Form):
#     frog_form = forms.CharField(max_length=200, label='Set new frog')

class SetFrogForm(forms.ModelForm):
    class Meta:
        model = Frog
        fields = ['name']


class SetTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'task_type']
