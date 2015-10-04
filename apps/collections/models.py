# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

sex = (('m', _(u'Мужские')), ('w', _(u'Женские')))


class Gallery(models.Model):
    class Meta:
        verbose_name = _(u"Коллекция")
        verbose_name_plural = _(u"Коллекции")
    year = models.IntegerField(verbose_name=_(u"Год"))
    name = models.CharField(max_length="256", verbose_name=_(u"Название"))

    image = models.ImageField(blank=True, null=True, verbose_name=_(u"Изображение для карусели"))
    image_url = models.URLField(blank=True, null=True, verbose_name=_(u"Сслыка изображения для карусели"))
    featured = models.BooleanField(default=True, verbose_name=_(u"Показывать в карусели"))

    def __unicode__(self):
        return "%s (%s)" % (self.name, self.year)


class Category(models.Model):
    class Meta:
        verbose_name = _(u"Категория")
        verbose_name_plural = _(u"Категории")
    name = models.CharField(max_length="256", verbose_name=_(u"Категория"))

    def __unicode__(self):
        return self.name


class GalleryImage(models.Model):
    image = models.ImageField(blank=True, null=True, verbose_name=_(u"Фотография"))
    image_small = models.ImageField(blank=True, null=True, verbose_name=_(u"Превью фотография"))

    image_url = models.URLField(blank=True, null=True, verbose_name=_(u"Ссылка на фотографию"))
    image_small_url = models.URLField(blank=True, null=True, verbose_name=_(u"Сллыка на превью фотографии"))

    title = models.CharField(max_length="256", blank=True, null=True, verbose_name=_(u"Заголовок"))
    model = models.CharField(max_length="256", blank=True, null=True, verbose_name=_(u"Модель"))
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name=_(u"Цена"))
    sex = models.CharField(max_length="256", blank=True, null=True, choices=sex, verbose_name=_(u"Пол"))

    category = models.ForeignKey(Category)
    gallery = models.ForeignKey(Gallery)

    recommended = models.BooleanField(default=False)

    def __unicode__(self):
        return u"%s: %s %s %s" % (self.category, self.title, self.sex, self.price)
