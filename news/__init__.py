
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

from .widget import *

default_app_config = 'news.Config'


class Default(object):

    optgroup = 'News'

    @property
    def apps(self):
        APPS = []
        try:
            import taggit
            APPS += ['taggit']
        except:
            pass
        apps = [
            'news',
            'articles',
        ]
        return apps + APPS

    widgets = [
        NewsWidget,
    ]

    plugins = [
        ('news.apps.news', _('News Articles')),
    ]

    absolute_url_overrides = {
        'articles.article': 'news.overrides.article'
    }


class Config(AppConfig, Default):
    name = 'news'
    verbose_name = _("News")

default = Default()
