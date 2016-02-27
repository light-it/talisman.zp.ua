from django.conf.urls import url

from .views import GalleryDetailView, GalleryWizard, GalleryHome, GalleryImagesEdit

urlpatterns = [
    url(r'^collections/(?P<pk>\d+)/$', GalleryDetailView.as_view(), name='collection-detail'),
    url(r'^collections/add/$', GalleryWizard.as_view(), name='collection-add'),
    url(r'^collections/(?P<pk>\d+)/edit/$', GalleryImagesEdit.as_view(), name='collection-edit'),
    url(r'^collections/$', GalleryHome.as_view(), name='collection-home'),
]