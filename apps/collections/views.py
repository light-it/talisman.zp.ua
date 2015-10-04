# -*- coding: utf-8 -*-
from django.views.generic import DetailView

from .models import Gallery


class GalleryDetailView(DetailView):
    template_name = 'collection_detail.html'
    model = Gallery

    def get_context_data(self, **kwargs):
        ctx = super(GalleryDetailView, self).get_context_data(**kwargs)
        ctx['for_man'] = self.object.galleryimage_set.filter(sex='m')
        ctx['for_woman'] = self.object.galleryimage_set.filter(sex='w')
        return ctx
