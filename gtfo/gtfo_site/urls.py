from django.conf.urls import patterns, url

urlpatterns = patterns(
    '',
    url(r"^(?P<host>[^/]+)$", "gtfo_site.views.handle_it"),
    url(r"^(?P<host>[^/]+)/(?P<path>.*)$", "gtfo_site.views.handle_it"),
)
