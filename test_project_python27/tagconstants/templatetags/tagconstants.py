"""
Setup:
    Add a dictionary, TAG_CONSTANTS, to settings.py,
    containing the constants you want to expose to the template
    layer. We use a white list this way as a security feature, since
    many constants, especially in settings.py, are of a sensitive nature.
    
Tags:

    constant:

        Input syntax 1:
            {% constant "CONSTANT_NAME" %}

        Output 1:
            str(TAG_CONSTANTS["CONSTANT_NAME"])

        Input syntax 2:
            {% constant "CONSTANT_NAME" as "variable_name" %}

        Output 2:
            loads the proper constant as a variable into the
            block's context. Returns the empty string as output.
"""

from django import template
from django.conf import settings

register = template.Library()

TAG_CONSTANTS = settings.TAG_CONSTANTS

@register.tag
def constant(parser, token):
    bits = token.split_contents()
    if len(bits) == 2:
        arg = bits[1]
        if(arg[0] == arg[-1] and arg[0] in ('"', "'")):
            return ConstantNode(constant=bits[1][1:-1])
        else:
           raise template.TemplateSyntaxError(
               "Malformed arguments to the {0} tag.".format(bits[0]) + 
               "Arguments must be in quotes.")
    if len(bits) == 4:
        arg = bits[1]
        if(arg[0] == arg[-1] and arg[0] in ('"', "'")):
            return ConstantNode(
                constant=bits[1][1:-1], asvar=bits[3])
        else:
            raise template.TemplateSyntaxError(
                "Malformed arguments to the {0} tag.".format(bits[0]) + 
                "Arguments must be in quotes.")
    else:
        raise template.TemplateSyntaxError(
            "{0} tag has been called with an improper number of arguments").format(
                bits[0])


class ConstantNode(template.Node):
    
    def __init__(self, constant, asvar=None):
        self.constant = constant
        self.asvar = asvar
        
    def render(self, context):
        if settings.DEBUG:
            # cause error in development
            try:
                if self.asvar:
                    context[self.asvar] = str(TAG_CONSTANTS[self.constant])
                    return ''
                else:
                    return str(TAG_CONSTANTS[self.constant])
            except KeyError:
                raise KeyError("No such constant exists in TAG_CONSTANTS dictionary")
        else:
            # fail silently in production
            try:
                if self.asvar:
                    context[self.asvar] = str(TAG_CONSTANTS[self.constant])
                    return ''
                else:
                    return str(TAG_CONSTANTS[self.constant])
            except:
                return ''
