from django.contrib import admin
from apps.ftp_import import models

admin.site.register(models.FTPConnect)
admin.site.register(models.FTPCollection)


