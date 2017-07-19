from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

urlpatterns = {
    url(r'^$', TeamsView.as_view(), name="teams"),
    url(r'^team/$', AddTeamView.as_view(), name="add-team"),
    url(r'^team/(?P<pk>[0-9]+)/player/$', AddPlayerView.as_view(), name="add-player"),
    url(r'^team/(?P<pk>[0-9]+)/$', TeamDetailsView.as_view(), name="team-details"),
    url(r'^log/$', LogView.as_view(), name="log"),
}

urlpatterns = format_suffix_patterns(urlpatterns)