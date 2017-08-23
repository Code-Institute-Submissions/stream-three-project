from base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# PayPal environment variables
SITE_URL = ''
PAYPAL_NOTIFY_URL = ''
PAYPAL_RECEIVER_EMAIL = 'nicole-merchant2@gmail.com'
