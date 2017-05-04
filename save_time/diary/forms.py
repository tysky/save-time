from django import forms
from .models import Frog, Task, Challenge, Steak, Joy, Memory


class DateTypeInput(forms.DateInput):
    input_type = 'date'


class ChooseDateForm(forms.Form):
    date_form = forms.DateField(label='Choose date', widget=DateTypeInput())


# class SetFrogForm(forms.Form):
#     frog_form = forms.CharField(max_length=200, label='Set new frog')

class SetChallengeForm(forms.ModelForm):
    class Meta:
        model = Challenge
        fields = ['name']


class SetFrogForm(forms.ModelForm):
    class Meta:
        model = Frog
        fields = ['name']


class SetSteakForm(forms.ModelForm):
    class Meta:
        model = Steak
        fields = ['name']


class SetTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'task_type']


class SetJoyForm(forms.ModelForm):
    class Meta:
        model = Joy
        fields = ['name']


class SetMemoryForm(forms.ModelForm):
    class Meta:
        model = Memory
        fields = ['name']
