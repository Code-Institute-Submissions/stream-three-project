from base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

SITE_URL = 'art-by-keryn.herokuapp.com'

# PayPal environment variables
PAYPAL_NOTIFY_URL = 'art-by-keryn.herokuapp.com/a-very-hard-to-guess-url/'
PAYPAL_RECEIVER_EMAIL = 'nicole-merchant2@gmail.com'
