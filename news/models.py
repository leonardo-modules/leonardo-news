
from django.utils.translation import ugettext_lazy as _

from articles.models import Article

from leonardo.module import media, web

Article.register_extensions('feincms.module.extensions.translations',
                            'feincms.module.extensions.datepublisher',
                            'articles.extensions.tags',
                            'articles.extensions.thumbnail',
                            )

REGIONS = ('main', 'preview',)

try:
    import taggit  # noqa
except:
    pass
else:
    Article.register_extensions(
        'articles.extensions.tags',
    )

Article.register_regions(
    ('preview', _('Preview area')),
    ('main', _('Main content area')),
)

Article.create_content_type(
    web.widget.HtmlTextWidget, regions=REGIONS, optgroup=_('Text'))
Article.create_content_type(
    web.widget.MarkupTextWidget, regions=REGIONS, optgroup=_('Text'))

for widget in media.default.widgets:
    Article.create_content_type(widget, regions=REGIONS, optgroup=_('Media'))

try:
    from leonardo_oembed.widget import OembedWidget
    Article.create_content_type(OembedWidget,
                                regions=REGIONS, optgroup=_('External content'))
except:
    pass
