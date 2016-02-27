from django.db import models


class FTPConnect(models.Model):
    """
    FTP connection
    """
    name = models.CharField(max_length=64)
    host = models.CharField(max_length=512)
    login = models.CharField(max_length=128)
    password = models.CharField(max_length=1024)

    def get_credentials_dict(self):
        """
        Return credentials dict for FTP client to connect
        :return:
        """
        return dict(host=self.host, passwd=self.password, user=self.login)

    def __unicode__(self):
        return self.name


class FTPCollection(models.Model):
    ftp = models.ForeignKey(FTPConnect)
    gallery = models.ForeignKey('collections.Gallery', null=True)
    name = models.CharField(max_length=256)
    base_url = models.URLField()
    base_directory = models.CharField(max_length=512)
    imported = models.BooleanField(default=False)
    updated_on = models.DateTimeField(null=True)
