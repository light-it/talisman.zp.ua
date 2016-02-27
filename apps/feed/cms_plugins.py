# -*- coding: utf-8 -*-
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from cmsplugin_newsplus.models import News


class NewsFeed(CMSPluginBase):
    model = CMSPlugin
    render_template = "feed.html"
    cache = False

    def render(self, context, instance, placeholder):
        ctx = super(NewsFeed, self).render(context, instance, placeholder)
        ctx['news'] = News.objects.all()[:10]
        return ctx


plugin_pool.register_plugin(NewsFeed)
