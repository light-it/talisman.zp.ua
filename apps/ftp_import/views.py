from django import forms
from django.http import HttpResponseRedirect
from django.views.generic import CreateView

from apps.ftp_import.models import FTPCollection
from apps.ftp_import.service import CollectionImporter

from django.core.urlresolvers import reverse


class FTPImportForm(forms.ModelForm):
    class Meta:
        model = FTPCollection
        fields = ('name', 'base_url', 'base_directory', 'ftp')


class FTPImportView(CreateView):
    form_class = FTPImportForm
    template_name = 'ftp_import.html'
    success_url = '/'

    def form_valid(self, form):
        super(FTPImportView, self).form_valid(form)
        ftp_collection = CollectionImporter(ftp_collection=form.instance).import_by_ftp()
        return HttpResponseRedirect(reverse('collection-edit', args=[ftp_collection.gallery.pk]))
