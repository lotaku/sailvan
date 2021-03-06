# -*- coding: UTF-8 –*-
import os
gettext = lambda s: s
DATA_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
"""
Django settings for mysite project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '4!8x(p@lnxg6k5b_+p%25m8d@l)(uperqd&qcs2=p^12kk=@rv'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition





ROOT_URLCONF = 'mysite.urls'

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases



# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'America/Chicago'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(DATA_DIR, 'media')
STATIC_ROOT = os.path.join(DATA_DIR, 'static')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'mysite', 'static'),
)
SITE_ID = 1

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware'
)

TEMPLATE_CONTEXT_PROCESSORS = (
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
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'mysite', 'templates'),
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
    'mptt',
    'djangocms_style',
    'djangocms_column',
    'djangocms_file',
    'djangocms_flash',
    'djangocms_googlemap',
    'djangocms_inherit',
	'django_select2',
    'djangocms_link',
    'djangocms_picture',
    'djangocms_teaser',
    'djangocms_video',
    'south',
    'reversion',
    'mysite',
	'djangocms_text_ckeditor',
	'easy_thumbnails',
	'filer',
	'taggit',
	'hvad',
    'mysite.content',
    'mysite.core',
    'ckeditor',
    'content_plugin',

)

LANGUAGES = (
    ## Customize this
    ('zh_CN', gettext('zh_CN')),
    ('en', gettext('en')),
    ('de', gettext('de')),

)
CMS_STYLE_NAMES = (
    ('info', gettext("info")),
    ('new', gettext("new")),
    ('hint', gettext("hint")),
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
            'code': 'zh_CN',
            'hide_untranslated': False,
            'name': gettext('zh_CN'),
            'redirect_on_fallback': True,
        },
        {
            'public': True,
            'code': 'en',
            'hide_untranslated': False,
            'name': gettext('en'),
            'redirect_on_fallback': True,
        },
        {
            'public': True,
            'code': 'de',
            'hide_untranslated': False,
            'name': gettext('de'),
            'redirect_on_fallback': True,
        },

    ],
}

CMS_TEMPLATES = (
    ## Customize this
    ('page.html', 'Page'),
    ('feature.html', 'Page with Feature'),
    ('footer_test.html', 'Page with footer'),
    ('index.html', 'Page with Index'),
    ('common_post.html', 'Common Post'),
    ('common_post_not_right_box.html', 'Common Post No Right'),
    ('index_1.html', 'Index_1'),
    ('index_2.html', 'Index_2'),
    ('index_3.html', 'Index_3'),
)

CMS_PERMISSION = True

CMS_PLACEHOLDER_CONF = {
	'common_post.html RB': {
        "plugins": ['CMSRightBoxPlugin'],
    },
	'common_post.html Post Boxes': {
        "plugins": ['CMSPostBoxPlugin'],
    },
	'common_post.html Globle RB': {
        "plugins": ['CMSRightBoxPlugin'],
    },

}

DATABASES = {
    'default':
        {'ENGINE': 'django.db.backends.sqlite3', 'NAME': 'project.db', 'HOST': 'localhost', 'USER': '', 'PASSWORD': '', 'PORT': ''}
}

SOUTH_MIGRATION_MODULES = {
    'easy_thumbnails': 'easy_thumbnails.south_migrations',
}

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    #'easy_thumbnails.processors.scale_and_crop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)




STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = (
	os.path.join(PROJECT_ROOT, 'static'),
    # os.path.join(BASE_DIR, "static"),
    # os.path.join(PROJECT_ROOT, "static"),
    # '/var/www/static/',
)
CKEDITOR_UPLOAD_PATH = "ckeditor_uploads/"
CKEDITOR_JQUERY_URL = 'http://code.jquery.com/jquery-1.7.2.min.js'

# 数据库备份
DBBACKUP_BACKUP_DIRECTORY = os.path.join(PROJECT_ROOT,'dbbackup')
# DBBACKUP_MEDIA_PATH = os.path.join(PROJECT_ROOT,'media_backup')
if not os.path.exists(DBBACKUP_BACKUP_DIRECTORY):
	os.mkdir(DBBACKUP_BACKUP_DIRECTORY)
# if not os.path.exists(DBBACKUP_MEDIA_PATH):
# 	os.mkdir(DBBACKUP_MEDIA_PATH)

#django-cms 自定义 by fzz
