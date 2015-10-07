# -*- coding: utf-8 -*-
from django.views.generic import DetailView, CreateView, ListView
from datetime import datetime
from .models import Gallery, GalleryImage

from django.forms import ModelForm
from django.forms.formsets import formset_factory


class CollectionForm(ModelForm):
    class Meta:
        model = Gallery
        fields = ['year', 'name', 'image', 'featured']


class ImageForm(ModelForm):
    class Meta:
        model = GalleryImage
        fields = ['image', 'title', 'model', 'price', 'sex', 'category']

ImageFormSet = formset_factory(ImageForm, extra=3, can_order=True)


class GalleryDetailView(DetailView):
    template_name = 'collection_detail.html'
    model = Gallery

    def get_context_data(self, **kwargs):
        ctx = super(GalleryDetailView, self).get_context_data(**kwargs)
        ctx['for_man'] = self.object.galleryimage_set.filter(sex='m')
        ctx['for_woman'] = self.object.galleryimage_set.filter(sex='w')
        return ctx


class GalleryHome(ListView):
    template_name = 'collections_home.html'
    queryset = Gallery.objects.order_by('-pk')


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
