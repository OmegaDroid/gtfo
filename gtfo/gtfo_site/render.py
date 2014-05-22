import os
from django.conf import settings
from django.http import HttpResponse, HttpResponseNotFound
from django.template import Template, Context


def _cache_path(host, url):
    hostCache = os.path.join(settings.GTFO_CACHE_DIR, host)

    if not url:
        return os.path.join(hostCache, "index")

    if url.startswith("/"):
        url = url[1:]

    if url.endswith("/"):
        url = url[:-1]

    return os.path.join(hostCache, *url.split("/"))


def _write_cached(path, render):
    d = os.path.dirname(path)

    os.makedirs(d)
    with open(path, "w") as f:
        f.write(render)


def _load_cached_response(host, url):
    with open(_cache_path(host, url), 'r') as f:
        return HttpResponse(content=f.read())


def _cached_version_exists(host, url):
    return os.path.exists(_cache_path(host, url))


def _create_response(host, url):
    t = settings.TEMPLATE_REGISTRY.get_template(url)
    if not t:
        return HttpResponseNotFound()

    templatePath = t["template"]
    context = {"host": host}
    context.update(t["context"])

    with open(templatePath, 'r') as f:
        template = Template(f.read())

    rendered = template.render(Context(context))

    _write_cached(_cache_path(host, url), rendered)

    return HttpResponse(content=rendered)


def render_response(host, url):
    if _cached_version_exists(host, url):
        return _load_cached_response(host, url)

    return _create_response(host, url)