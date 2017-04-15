from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Frog, Day

# Create your views here.
@login_required
def index(request):
    num_frogs = Frog.objects.count()
    owner_frogs = Frog.objects.filter(user=request.user).get()
    day = Day.objects.filter(user=request.user).get()
    day_frog = Day.objects.filter(user=request.user).get()
    return render(request, 'index.html', context={'word': 'atatattatat',
                                                  'num_frogs': num_frogs,
                                                  'owner_frogs': owner_frogs,
                                                  'day': day,
                                                  'day_frog': day_frog})