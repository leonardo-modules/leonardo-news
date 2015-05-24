
from django.db import models
from django.utils.translation import ugettext_lazy as _

from leonardo.module.web.models import Widget

from articles.models import Article


class NewsWidget(Widget):

    number = models.IntegerField()
    show_archive_button = models.BooleanField(
        default=True, verbose_name=_("show archive button"))

    def get_news(self):
        return Article.objects.all()

    class Meta:
        abstract = True
        verbose_name = _("last news")
        verbose_name_plural = _("last news")
