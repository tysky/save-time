from django import forms

class DateTypeInput(forms.DateInput):
    input_type = 'date'


class ChooseDateForm(forms.Form):
    date_form = forms.DateField(label='Choose date', widget=DateTypeInput())
