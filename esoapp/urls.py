from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView
from esoapp.models import Poll
from django.utils import timezone

urlpatterns = patterns('',
    url(r'^$',
        ListView.as_view(
            queryset=Poll.objects.filter(pub_date__lte=timezone.now)\
                                 .order_by('-pub_date')[:5],
            context_object_name='latest_poll_list',
            template_name='esoapp/index.html'),
        name='index'),
    url(r'^(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Poll,
            template_name='esoapp/detail.html'),
        name='detail'),
    url(r'^(?P<pk>\d+)/results/$',
        DetailView.as_view(
            model=Poll,
            template_name='esoapp/results.html'),
        name='results'),
    url(r'^(?P<poll_id>\d+)/vote/$', 'esoapp.views.vote', name='vote'),
)