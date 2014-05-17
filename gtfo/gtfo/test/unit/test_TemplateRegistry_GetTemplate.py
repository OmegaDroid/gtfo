from django.test import TestCase
from gtfo.registry import TemplateRegistry


class TemplateRegistry_GetTemplate(TestCase):
    def test_NoTemplatesRegistered_ReturnsNone(self):
        reg = TemplateRegistry({})

        self.assertEqual(None, reg.get_template("foo"))

    def test_UrlDoesNotMatchAnyRegisteredRegexes_ReturnIsNone(self):
        reg = TemplateRegistry({"foo": "bar"})

        self.assertEqual(None, reg.get_template("boo"))

    def test_UrlMatchesRegexWithNoGroups_ReturnHasTheTemplateNameNoContextValues(self):
        reg = TemplateRegistry({"foo": "bar"})

        expected = {
            "template": "bar",
            "context": {}
        }

        self.assertEqual(expected, reg.get_template("foo"))

    def test_UrlMatchesRegexWithNamedGroup_ReturnHasTheTemplateNameContextValue(self):
        reg = TemplateRegistry({"(?P<var>.*?)foo": "bar"})

        expected = {
            "template": "bar",
            "context": {
                "var": "val"
            }
        }

        self.assertEqual(expected, reg.get_template("valfoo"))

    def test_UrlMatchesRegexWithMultipleNamedGroups_ReturnHasTheTemplateNameContextValues(self):
        reg = TemplateRegistry({"^(?P<var>.*?)foo(?P<var2>.*?)$": "bar"})

        expected = {
            "template": "bar",
            "context": {
                "var": "val",
                "var2": "val2"
            }
        }

        self.assertEqual(expected, reg.get_template("valfooval2"))
