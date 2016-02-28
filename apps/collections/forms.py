# -*- coding: utf-8 -*-
from django import forms

from .models import Gallery, GalleryImage, SEX_CHOICES


class CollectionForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(), label=u'Описание')

    class Meta:
        model = Gallery
        fields = ['year', 'name', 'image', 'featured', 'description']


class ImageForm(forms.ModelForm):

    class Meta:
        model = GalleryImage
        fields = ['image', 'title', 'model', 'price', 'sex', 'category']


class ExternalImageForm(forms.ModelForm):
    sex = forms.ChoiceField(widget=forms.RadioSelect, choices=SEX_CHOICES, label=u'Пол')

    class Meta:
        model = GalleryImage
        fields = ['title', 'model', 'price', 'sex', 'category']
