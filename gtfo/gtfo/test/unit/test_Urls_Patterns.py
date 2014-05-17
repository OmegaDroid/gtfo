from django.core.urlresolvers import resolve
from django.http import Http404
from django.test import TestCase

from gtfo.views import handle_it


class Urls_Patterns(TestCase):
    def test_UrlIsEmptyString_ResponseIs404(self):
        self.assertRaises(Http404, resolve, "")

    def test_UrlHasOnlyTheTargetHostname_ResponseFunctionIsHandleIt(self):
        resolver = resolve("/foo")

        self.assertEqual(handle_it, resolver.func)

    def test_UrlHasOnlyTheTargetHostname_ResponseHasOneKwargHostFoo(self):
        resolver = resolve("/foo")

        self.assertEqual({"host": "foo"}, resolver.kwargs)

    def test_UrlHasTheTargetHostnameAndPath_ResponseHasOnePathKwarg(self):
        resolver = resolve("/foo/this/is/my/path")

        self.assertEqual({"host": "foo", "path": "this/is/my/path"}, resolver.kwargs)