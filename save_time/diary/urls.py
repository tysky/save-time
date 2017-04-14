from django.conf.urls import url
from django.conf.urls import include

from datetime import date

from . import views

# define current day in format yyyy-mm-dd
today = "{0}-{1}-{2}".format(date.today().year, date.today().month, date.today().day)

urlpatterns = [
    url('^accounts/', include('django.contrib.auth.urls')),
    url(today, views.index, name='index'),
    # url(r'^$', views.index, name='index'),
]