from django.test import TestCase
from django.test.utils import override_settings
from django.template import Template, Context


@override_settings(TAG_CONSTANTS={'A_CONSTANT': 'A VALUE'}, 
                   SECRET='A SECRET')
class ConstantTagTests(TestCase):
    """test cases for the 'constant' template tag."""

    def test_loads_constant_to_context(self):
        """test that the constant tag can load a constant
        into the template's context.
        """
        t = Template("{% load tagconstants %}" 
                     "{% constant 'A_CONSTANT' as var %}")
        c = Context({})
        t.render(c)
        self.assertEqual(c['var'], 'A VALUE')

    def test_renders_to_constant(self):
        """test that the constant tag renders."""
        t = Template("{% load tagconstants %}" 
                     "{% constant 'A_CONSTANT' %}")
        c = Context({})
        self.assertIn('A VALUE', t.render(c))

    def test_doesnt_get_settings_not_in_tag_constants(self):
        """test that the constant tag doesn't have access to
        constants from the settings file that are not explicitly
        in the TAG_CONSTANTS dictionary.
        """
        t = Template("{% load tagconstants %}" 
                     "{% constant 'SECRET' %}")
        c = Context({})
        self.assertNotIn('A SECRET', t.render(c))
