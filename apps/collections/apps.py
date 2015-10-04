# -*- coding: utf-8 -*-
__author__ = 'fennel'
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class GalleryConfig(AppConfig):
    name = 'collections'
    verbose_name = _(u"Колелкции")
