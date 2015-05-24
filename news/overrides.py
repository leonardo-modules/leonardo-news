
def article(self):
    from leonardo.module.web.widget.application.reverse import app_reverse
    return app_reverse(
        'article_detail',
        'news.apps.news',
        kwargs={
            'slug': self.slug,
        })
