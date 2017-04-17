from datetime import date

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic


from .models import Frog, Day, Task

today = date.today()


# Create your views here.
@login_required
def index(request, url_day=str(today)):
    num_frogs = Frog.objects.filter(user=request.user).count()
    frogs = Frog.objects.filter(user=request.user, day__date=url_day)
    tasks = Task.objects.filter(user=request.user, day__date=url_day)
    day = Day.objects.filter(date=url_day).get()
    return render(request, 'index.html', context={'word': 'atatattatat',
                                                  'num_frogs': num_frogs,
                                                  'frogs': frogs,
                                                  'tasks': tasks,
                                                  'day': day,
                                                  'url_day': url_day,
                                                  })


# class DayDetailView(generic.DetailView):
#
#     template_name = 'index_detail.html'
#     model = Day

