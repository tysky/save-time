from django.conf.urls import url
from django.conf.urls import include
from django.views.generic import RedirectView

from datetime import date

from . import views

# define current day in format yyyy-mm-dd
today = "{0}-{1}-{2}".format(date.today().year, date.today().month, date.today().day)


urlpatterns = [
    url('^accounts/', include('django.contrib.auth.urls')),
    # url(r'^day/'+today, views.index, name='index'),
    url(r'^day/(?P<url_day>\d{4}-\d{1,2}-\d{1,2})/$', views.index, name='index'),
    # url(r'^day/(?P<pk>\d+)$', views.DayDetailView.as_view(), name='index'),
    # url(r'^day/(?P<{0}>){1}'.format('2', today), views.DayDetailView.as_view(), name='index'),
    url(r'^$', RedirectView.as_view(url='/day/'+today)),
    # url(r'^$', views.index, name='index'),
]