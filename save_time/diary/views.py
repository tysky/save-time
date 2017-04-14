from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Frog

# Create your views here.
@login_required
def index(request):
    num_frogs = Frog.objects.count()
    owner_frogs = Frog.objects.filter(owner=request.user).get()
    return render(request, 'index.html', context={'word': 'atatattatat',
                                                  'num_frogs': num_frogs,
                                                  'owner_frogs': owner_frogs})