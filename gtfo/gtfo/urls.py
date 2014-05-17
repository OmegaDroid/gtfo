from django.conf.urls import patterns, url

urlpatterns = patterns(
    '',
    url(r"^(?P<host>[^/]+)$", "gtfo.views.handle_it"),
    url(r"^(?P<host>[^/]+)/(?P<path>.*)$", "gtfo.views.handle_it"),
)
