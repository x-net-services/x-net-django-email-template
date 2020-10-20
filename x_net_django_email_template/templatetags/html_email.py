import logging

from django import template
from django.templatetags import static


register = template.Library()

################################################################################
# LOGGER

logger = logging.getLogger(__name__)


################################################################################
# FULL STATIC

class FullStaticNode(static.StaticNode):
    def url(self, context):
        request = context["request"]
        return request.build_absolute_uri(super().url(context))


@register.tag
def full_static(parser, token):
    return FullStaticNode.handle_token(parser, token)
