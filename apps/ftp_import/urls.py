from django.conf.urls import url
from apps.ftp_import.views import FTPImportView


urlpatterns = [
    url(r'^import/$', FTPImportView.as_view(), name='ftp-collection-import'),
]
