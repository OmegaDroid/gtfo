import os
from django.http import HttpResponseNotFound
from django.test import TestCase
from django.conf import settings
from shutil import rmtree
from gtfo.gtfo_site.registry import load_registry
from gtfo.gtfo_site.render import render_response


class Render_RenderResponse(TestCase):
    def setUp(self):
        load_registry(os.path.join(os.path.dirname(__file__), "test_templates", "test_registry.json"))

    def tearDown(self):
        if settings.GTFO_CACHE_DIR and os.path.exists(settings.GTFO_CACHE_DIR):
            rmtree(settings.GTFO_CACHE_DIR)

    def test_UrlDoesNotMatchAnything_ResultIs404(self):
        response = render_response("host", "404url")

        self.assertTrue(isinstance(response, HttpResponseNotFound))

    def test_LoadHostHome_HelloTemplateIsLoaded(self):
        response = render_response("host", "")

        self.assertEqual(b"hello world", response.content)

    def test_LoadHostHome_CachedVersionInTheHostExists(self):
        render_response("host", "")

        cachePath = os.path.join(settings.GTFO_CACHE_DIR, "host", "index")

        self.assertTrue(os.path.exists(cachePath))

    def test_LoadHostHomeForDifferenctHosts_CachedVersionInBothHostExists(self):
        render_response("host1", "")
        render_response("host2", "")

        cachePath1 = os.path.join(settings.GTFO_CACHE_DIR, "host1", "index")
        cachePath2 = os.path.join(settings.GTFO_CACHE_DIR, "host2", "index")

        self.assertTrue(os.path.exists(cachePath1))
        self.assertTrue(os.path.exists(cachePath2))

    def test_LoadHostHomeTwice_HelloTemplateIsLoaded(self):
        render_response("host", "")
        response = render_response("host", "")

        self.assertEqual(b"hello world", response.content)

    def test_LoadFileWithTwoParams_ResponseHasTheCorrectContent(self):
        response = render_response("host", "1/2/foo")

        self.assertEqual(b"first = 1, second = 2", response.content)

    def test_LoadFileWithTwoParams_CachedVersionInTheHostExists(self):
        render_response("host", "1/2/foo")

        cachePath = os.path.join(settings.GTFO_CACHE_DIR, "host", "1", "2", "foo")

        self.assertTrue(os.path.exists(cachePath))

    def test_LoadFileWithTwoParamsTwiceWithDifferentParams_BothCachedVersionInTheHostExists(self):
        render_response("host", "1/2/foo")
        render_response("host", "3/4/foo")

        cachePath1 = os.path.join(settings.GTFO_CACHE_DIR, "host", "1", "2", "foo")
        cachePath2 = os.path.join(settings.GTFO_CACHE_DIR, "host", "3", "4", "foo")

        self.assertTrue(os.path.exists(cachePath1))
        self.assertTrue(os.path.exists(cachePath2))