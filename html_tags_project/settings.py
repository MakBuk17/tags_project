
SECRET_KEY = 'django-insecure-xyz'
DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',
    'tags',
]

ROOT_URLCONF = 'html_tags_project.urls'

TEMPLATES = [{'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [f"/mnt/data/html_tags_project/html_tags_project/templates"],
    'APP_DIRS': True}]

WSGI_APPLICATION = 'html_tags_project.wsgi.application'

STATIC_URL = '/static/'
