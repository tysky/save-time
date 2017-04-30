from datetime import date, timedelta

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


from .models import Frog, Day, Task
from .forms import ChooseDateForm, SetFrogForm

today = date.today()

# Create your views here.
@login_required
def index(request, url_day=str(today)):
    num_frogs = Frog.objects.filter(user=request.user).count()
    frogs = Frog.objects.filter(user=request.user, day__date=url_day)
    tasks = Task.objects.filter(user=request.user, day__date=url_day)
    day = Day.objects.filter(date=url_day).get()

    prev_day = day.date - timedelta(days=1)
    next_day = day.date + timedelta(days=1)
    # yesterday = Day.objects.filter(date=yes_arg)

    if request.method == 'POST':
        form_choose_date = ChooseDateForm(request.POST)
        form_set_frog = SetFrogForm(request.POST)

        if form_choose_date.is_valid():
            date_form = form_choose_date.cleaned_data['date_form']
            return HttpResponseRedirect('/day/{0}/'.format(date_form))

        if form_set_frog.is_valid():
            day_inst = get_object_or_404(Day, date=url_day)
            frog_name = form_set_frog.cleaned_data['name']
            new_day = Frog.objects.create(name=frog_name, user=request.user,
                                          done=False, day=day_inst)
            new_day.save()
            return HttpResponseRedirect('/day/{0}/'.format(url_day))

    else:
        form_choose_date = ChooseDateForm(initial={'date_form': today})
        form_set_frog = SetFrogForm()
    return render(request, 'index.html', context={'word': 'atatattatat',
                                                  'num_frogs': num_frogs,
                                                  'frogs': frogs,
                                                  'tasks': tasks,
                                                  'day': day,
                                                  'url_day': url_day,
                                                  'form_date': form_choose_date,
                                                  'form_frog': form_set_frog,
                                                  'prev_day': prev_day,
                                                  'next_day': next_day,
                                                  })


def choose_date(request):
    if request.method == 'POST':
        form = ChooseDateForm(request.POST)
        if form.is_valid():
            date_form = form.cleaned_data['date_form']
            return HttpResponseRedirect('/{0}/'.format(date_form))
    # else:
    #     form = ChooseDateForm()
    # return render(request, 'index', {'form': form})

# class DayDetailView(generic.DetailView):
#
#     template_name = 'index_detail.html'
#     model = Day

