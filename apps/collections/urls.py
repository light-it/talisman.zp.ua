from django.conf.urls import url

from .views import GalleryDetailView

urlpatterns = [
    url(r'^collections/(?P<pk>\d+)/$', GalleryDetailView.as_view(), name='collection-detail'),
]