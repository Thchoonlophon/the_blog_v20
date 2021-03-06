# -*- coding: utf-8 -*-

from django.conf import settings
from .utils import site_full_url


# 自定义上下文管理器
def settings_info(request):
    return {
        'site_description': settings.SITE_DESCRIPTION,
        'site_keywords': settings.SITE_KEYWORDS,
        'tool_flag': settings.TOOL_FLAG,
        'api_flag': settings.API_FLAG,
        'site_url': site_full_url(),
    }
