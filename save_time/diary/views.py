from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic


from .models import Frog, Day

# Create your views here.
# @login_required
# def index(request):
#     num_frogs = Frog.objects.count()
#     owner_frogs = Frog.objects.filter(user=request.user)
#     day = Day.objects.filter(user=request.user).get()
#     day_frog = Day.objects.filter(user=request.user)
#     return render(request, 'index.html', context={'word': 'atatattatat',
#                                                   'num_frogs': num_frogs,
#                                                   'owner_frogs': owner_frogs,
#                                                   'day': day,
#                                                   'day_frog': day_frog})


class DayDetailView(generic.DetailView):

    template_name = 'index_detail.html'
    model = Day

