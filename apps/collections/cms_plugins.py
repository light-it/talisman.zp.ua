# -*- coding: utf-8 -*-
__author__ = 'fennel'
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin

from .models import Gallery, GalleryImage


class CollectionsListPlugin(CMSPluginBase):
    model = CMSPlugin
    render_template = "collections.html"
    cache = False

    def render(self, context, instance, placeholder):
        ctx = super(CollectionsListPlugin, self).render(context, instance, placeholder)
        ctx['collections'] = Gallery.objects.all()[:10]
        ctx['total'] = Gallery.objects.count()
        return ctx


class CollectionsCarousel(CMSPluginBase):
    model = CMSPlugin
    render_template = "carousel.html"
    cache = False

    def render(self, context, instance, placeholder):
        ctx = super(CollectionsCarousel, self).render(context, instance, placeholder)
        ctx['collections'] = Gallery.objects.filter(featured=True)
        return ctx

plugin_pool.register_plugin(CollectionsListPlugin)
plugin_pool.register_plugin(CollectionsCarousel)
