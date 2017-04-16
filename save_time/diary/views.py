from datetime import date

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic


from .models import Frog, Day, Task

# Create your views here.
@login_required
def index(request):
    num_frogs = Frog.objects.filter(user=request.user).count()
    frogs = Frog.objects.filter(user=request.user)
    tasks = Task.objects.filter(user=request.user)
    day = Day.objects.filter(date=date.today()).get()
    return render(request, 'index.html', context={'word': 'atatattatat',
                                                  'num_frogs': num_frogs,
                                                  'frogs': frogs,
                                                  'tasks': tasks,
                                                  'day': day,
                                                  })


# class DayDetailView(generic.DetailView):
#
#     template_name = 'index_detail.html'
#     model = Day

