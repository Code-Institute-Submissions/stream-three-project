from base import *

DEBUG = True

INSTALLED_APPS.append('debug_toolbar')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


SITE_URL = 'http://127.0.0.1:8000'

# PayPal Settings
PAYPAL_NOTIFY_URL = 'http://f6d86620.ngrok.io/a-very-hard-to-guess-url/'
PAYPAL_RECEIVER_EMAIL = 'nicole-merchant2@gmail.com'
