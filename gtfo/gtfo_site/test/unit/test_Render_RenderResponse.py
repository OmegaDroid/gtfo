try:
    from unittest.mock import Mock, patch
except ImportError:
    from mock import patch, Mock
from django.test import TestCase
from gtfo.gtfo_site.render import render_response
import gtfo


class Render_RenderResponse(TestCase):
    @patch('gtfo.gtfo_site.render._load_cached_response', Mock())
    @patch('gtfo.gtfo_site.render._cached_version_exists', Mock(return_value=True))
    def test_CachedVersionExists_LoadCachedResponseIsCalled(self):
        render_response("host", "foo")

        gtfo.gtfo_site.render._load_cached_response.assert_called_once_with("host", "foo")


    @patch('gtfo.gtfo_site.render._create_response', Mock())
    @patch('gtfo.gtfo_site.render._cached_version_exists', Mock(return_value=False))
    def test_CachedVersionDoesNotExists_CreateResponseIsCalled(self):
        render_response("host", "foo")

        gtfo.gtfo_site.render._create_response.assert_called_once_with("host", "foo")