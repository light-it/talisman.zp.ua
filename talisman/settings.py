import os

import dj_database_url

gettext = lambda s: s

DATA_DIR = os.path.dirname(os.path.dirname(__file__))
"""
Django settings for talisman project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'hf&(sh_gi=0qgk=^ip3-z%4lq9=1+zqsdz7ot#42tp9e+*8v_m'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['talisman.herokuapp.com', 'talisman.zp.ua']


# Application definition

ROOT_URLCONF = 'talisman.urls'
WSGI_APPLICATION = 'talisman.wsgi.application'


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Europe/Zaporozhye'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(DATA_DIR, 'media')
STATIC_ROOT = os.path.join(DATA_DIR, 'static')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'talisman', 'static'),
)

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

SITE_ID = 1


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'OPTIONS': {
            'debug': True,
            'context_processors':
                (
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                    'django.core.context_processors.i18n',
                    'django.core.context_processors.debug',
                    'django.core.context_processors.request',
                    'django.core.context_processors.media',
                    'django.core.context_processors.csrf',
                    'django.core.context_processors.tz',
                    'sekizai.context_processors.sekizai',
                    'django.core.context_processors.static',
                    'cms.context_processors.cms_settings'
                ),
            'loaders':
                (
                    'django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader',
                    'django.template.loaders.eggs.Loader'
                )
        }
    },
]

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware'
)

INSTALLED_APPS = (
    'djangocms_admin_style',
    'djangocms_text_ckeditor',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'cms',
    'menus',
    'sekizai',
    'treebeard',
    'djangocms_style',
    'djangocms_column',
    'djangocms_file',
    'djangocms_flash',
    'djangocms_googlemap',
    'djangocms_inherit',
    'djangocms_link',
    'djangocms_picture',
    'djangocms_teaser',
    'djangocms_video',
    'cmsplugin_newsplus',
    'bootstrapform',
    'reversion',
    'talisman',
    'apps.feed',
    'apps.ftp_import',
    'apps.collections',

)

THUMBNAIL_PROCESSORS = (
    'cmsplugin_nivoslider.thumbnail_processors.pad_image',
)

LANGUAGES = (
    ## Customize this
    ('ru', gettext('ru')),
)

CMS_LANGUAGES = {
    ## Customize this
    'default': {
        'public': True,
        'hide_untranslated': False,
        'redirect_on_fallback': True,
    },
    1: [
        {
            'public': True,
            'code': 'ru',
            'hide_untranslated': False,
            'name': gettext('ru'),
            'redirect_on_fallback': True,
        },
    ],
}

CMS_TEMPLATES = (
    ## Customize this
    ('page.html', 'Page'),
    ('feature.html', 'Page with Feature')
)

CMS_PERMISSION = True

CMS_PLACEHOLDER_CONF = {}

DATABASES = {
    'default': dj_database_url.parse(url=os.environ.get('DATABASE_URL'))
}

MIGRATION_MODULES = {
    'djangocms_flash': 'djangocms_flash.migrations_django',
    'djangocms_file': 'djangocms_file.migrations_django',
    'djangocms_inherit': 'djangocms_inherit.migrations_django',
    'djangocms_column': 'djangocms_column.migrations_django',
    'djangocms_video': 'djangocms_video.migrations_django',
    'djangocms_picture': 'djangocms_picture.migrations_django',
    'djangocms_googlemap': 'djangocms_googlemap.migrations_django',
    'djangocms_style': 'djangocms_style.migrations_django',
    'djangocms_teaser': 'djangocms_teaser.migrations_django'
}


try:
    from talisman.local import *
except ImportError:
    pass
