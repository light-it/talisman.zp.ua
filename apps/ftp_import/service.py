from datetime import date, datetime
from ftplib import FTP
from apps.collections.models import Gallery, GalleryImage


class CollectionImporter(object):
    """
    Helps to import collection from FTP
    It scans the folder to collect image list and generates collection based on it
    """
    def __init__(self, ftp_collection):
        self.ftp_collection = ftp_collection
        self.base_url = ftp_collection.base_url
        self.gallery_name = ftp_collection.name
        self.base_directory = ftp_collection.base_directory

        if not self.base_url[-1] == '/':
            self.base_url = '{}/'.format(self.base_url)

    def import_by_ftp(self):
        """
        Import data by FTP and update the ftp collection object
        :return:
        """
        connect_instance = self.ftp_collection.ftp
        ftp = FTP(**connect_instance.get_credentials_dict())

        big_images, small_images = self._get_images_list(ftp)

        gallery = self._create_category(big_images, small_images)
        self._update_instance(gallery)
        return self.ftp_collection

    def _update_instance(self, gallery):
        self.ftp_collection.imported = True
        self.ftp_collection.gallery = gallery
        self.ftp_collection.updated_on = datetime.now()
        self.ftp_collection.save()

    def _get_images_list(self, ftp):
        big_images = ftp.nlst('{}/b'.format(self.base_directory))
        small_images = ftp.nlst('{}/s'.format(self.base_directory))
        return big_images, small_images

    def _create_category(self, big_images, small_images):
        gallery = Gallery.objects.create(name=self.gallery_name, year=date.today().year)
        for img in big_images:
            GalleryImage.objects.create(
                image_url=self._get_big_image_url(img),
                image_small_url=self._get_small_image_url(img, small_images),
                gallery=gallery
            )
        return gallery

    def _get_small_image_url(self, img, small_images):
        return '{}{}/{}/{}'.format(self.base_url, self.base_directory, 's' if img in small_images else 'b', img)

    def _get_big_image_url(self, img):
        return '{}{}/b/{}'.format(self.base_url, self.base_directory, img)
