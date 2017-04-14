from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Frog

# Create your views here.
@login_required
def index(request):
    num_frogs = Frog.objects.count()
    frogs = Frog.objects
    return render(request, 'index.html', context={'word': 'atatattatat',
                                                  'num_frogs': num_frogs, 
                                                  'frogs': frogs})