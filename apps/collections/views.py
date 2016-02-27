# -*- coding: utf-8 -*-
from datetime import datetime

from django.forms import modelformset_factory
from django.forms.formsets import formset_factory
from django.views.generic import DetailView, CreateView, ListView, UpdateView

from .forms import CollectionForm, ImageForm, ExternalImageForm
from .models import Gallery, GalleryImage

ImageFormSet = formset_factory(ImageForm, extra=3, can_order=True)
ModelImageFormset = modelformset_factory(GalleryImage, ExternalImageForm, can_delete=True)


class GalleryDetailView(DetailView):
    template_name = 'collection_detail.html'
    model = Gallery

    def get_context_data(self, **kwargs):
        ctx = super(GalleryDetailView, self).get_context_data(**kwargs)
        ctx['for_man'] = self.object.galleryimage_set.filter(sex='m')
        ctx['for_woman'] = self.object.galleryimage_set.filter(sex='w')
        ctx['other'] = self.object.galleryimage_set.filter(sex__isnull=True)
        return ctx


class GalleryHome(ListView):
    template_name = 'collections_home.html'
    queryset = Gallery.objects.order_by('-pk')


class GalleryImagesEdit(UpdateView):
    template_name = 'wizard/collection_edit.html'
    form_class = CollectionForm
    model = Gallery

    def post(self, request, *args, **kwargs):
        main_form = CollectionForm(data=request.POST, files=request.FILES)
        image_forms = ModelImageFormset(request.POST, request.FILES)

        if image_forms.is_valid() and main_form.is_valid():
            image_forms.save()

        return super(GalleryImagesEdit, self).post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        ctx = super(GalleryImagesEdit, self).get_context_data(**kwargs)
        ctx['image_formset'] = ModelImageFormset(queryset=self.object.galleryimage_set.all())
        return ctx


class GalleryWizard(CreateView):
    template_name = 'wizard/collection_wizard.html'
    form_class = CollectionForm
    success_url = '/'

    def post(self, request, *args, **kwargs):
        main_form = CollectionForm(data=request.POST, files=request.FILES)
        image_forms = ImageFormSet(request.POST, request.FILES)

        if image_forms.is_valid() and main_form.is_valid():
            gallery = main_form.save()

            for image in image_forms:
                image.instance.gallery = gallery
                image.save()

            return self.form_valid(main_form)

        return self.form_invalid(main_form)

    def get_context_data(self, **kwargs):
        ctx = super(GalleryWizard, self).get_context_data(**kwargs)
        ctx['image_form'] = ImageForm()
        ctx['image_formset'] = ImageFormSet()
        return ctx

    def get_initial(self):
        return {
            'year': datetime.now().year
        }
