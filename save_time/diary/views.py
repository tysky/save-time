from datetime import date, timedelta

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


from .models import Challenge, Frog, Day, Task, Steak, Joy, Memory
from .forms import ChooseDateForm, SetFrogForm, SetTaskForm, SetChallengeForm, SetSteakForm, SetJoyForm, SetMemoryForm

today = date.today()


# Create your views here.
@login_required
def index(request, url_day=str(today)):
    challenge = Challenge.objects.filter(user=request.user, day__date=url_day)
    frogs = Frog.objects.filter(user=request.user, day__date=url_day)
    steak = Steak.objects.filter(user=request.user, day__date=url_day)
    tasks = Task.objects.filter(user=request.user, day__date=url_day)
    joy = Joy.objects.filter(user=request.user, day__date=url_day)
    memory = Memory.objects.filter(user=request.user, day__date=url_day)
    day = Day.objects.filter(date=url_day).get()

    prev_day = day.date - timedelta(days=1)
    next_day = day.date + timedelta(days=1)
    # yesterday = Day.objects.filter(date=yes_arg)

    if request.method == 'POST' and 'btndate' in request.POST:
        form_choose_date = ChooseDateForm(request.POST)

        if form_choose_date.is_valid():
            date_form = form_choose_date.cleaned_data['date_form']
            return HttpResponseRedirect('/day/{0}/'.format(date_form))

    elif request.method == 'POST' and 'btntask' in request.POST:
        form_set_task = SetTaskForm(request.POST)

        if form_set_task.is_valid():
            day_inst = get_object_or_404(Day, date=url_day)
            task_name = form_set_task.cleaned_data['name']
            task_type = form_set_task.cleaned_data['task_type']
            new_task = Task.objects.create(name=task_name, user=request.user,
                                           task_type=task_type, day=day_inst)
            new_task.save()
            return HttpResponseRedirect('/day/{0}/'.format(url_day))

    elif request.method == 'POST' and 'btn-challenge' in request.POST:
        form_set_challenge = SetChallengeForm(request.POST)

        if form_set_challenge.is_valid():
            day_inst = get_object_or_404(Day, date=url_day)
            challenge_name = form_set_challenge.cleaned_data['name']
            new_day = Challenge.objects.create(name=challenge_name, user=request.user,
                                          day=day_inst)
            new_day.save()
            return HttpResponseRedirect('/day/{0}/'.format(url_day))

    elif request.method == 'POST' and 'btn-frog' in request.POST:
        form_set_frog = SetFrogForm(request.POST)

        if form_set_frog.is_valid():
            day_inst = get_object_or_404(Day, date=url_day)
            frog_name = form_set_frog.cleaned_data['name']
            new_day = Frog.objects.create(name=frog_name, user=request.user,
                                          done=False, day=day_inst)
            new_day.save()
            return HttpResponseRedirect('/day/{0}/'.format(url_day))

    elif request.method == 'POST' and 'btn-steak' in request.POST:
        form_set_steak = SetSteakForm(request.POST)

        if form_set_steak.is_valid():
            day_inst = get_object_or_404(Day, date=url_day)
            steak_name = form_set_steak.cleaned_data['name']
            new_day = Steak.objects.create(name=steak_name, user=request.user,
                                          day=day_inst)
            new_day.save()
            return HttpResponseRedirect('/day/{0}/'.format(url_day))

    elif request.method == 'POST' and 'btn-joy' in request.POST:
        form_set_joy = SetJoyForm(request.POST)

        if form_set_joy.is_valid():
            day_inst = get_object_or_404(Day, date=url_day)
            joy_name = form_set_joy.cleaned_data['name']
            new_day = Joy.objects.create(name=joy_name, user=request.user,
                                          day=day_inst)
            new_day.save()
            return HttpResponseRedirect('/day/{0}/'.format(url_day))

    elif request.method == 'POST' and 'btn-memory' in request.POST:
        form_set_memory = SetMemoryForm(request.POST)

        if form_set_memory.is_valid():
            day_inst = get_object_or_404(Day, date=url_day)
            memory_name = form_set_memory.cleaned_data['name']
            new_day = Memory.objects.create(name=memory_name, user=request.user,
                                          day=day_inst)
            new_day.save()
            return HttpResponseRedirect('/day/{0}/'.format(url_day))

    else:
        form_choose_date = ChooseDateForm(initial={'date_form': today})
        form_set_challenge = SetChallengeForm()
        form_set_frog = SetFrogForm()
        form_set_steak = SetSteakForm()
        form_set_task = SetTaskForm()
        form_set_joy = SetJoyForm()
        form_set_memory = SetMemoryForm()

    return render(request, 'diary/index.html', context={
                                                  'challenge': challenge,
                                                  'frogs': frogs,
                                                  'tasks': tasks,
                                                  'steak': steak,
                                                  'joy': joy,
                                                  'memory': memory,
                                                  'day': day,
                                                  'url_day': url_day,
                                                  'form_date': form_choose_date,
                                                  'form_challenge': form_set_challenge,
                                                  'form_frog': form_set_frog,
                                                  'form_steak': form_set_steak,
                                                  'form_task': form_set_task,
                                                  'form_joy': form_set_joy,
                                                  'form_memory': form_set_memory,
                                                  'prev_day': prev_day,
                                                  'next_day': next_day,
                                                  'today': today,
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

