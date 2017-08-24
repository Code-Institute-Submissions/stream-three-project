from base import *

DEBUG = False

INSTALLED_APPS.append('debug_toolbar')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# PayPal Settings
SITE_URL = 'heroku'
PAYPAL_NOTIFY_URL = 'heroku/a-very-hard-to-guess-url/'
PAYPAL_RECEIVER_EMAIL = 'nicole-merchant2@gmail.com'
