from base import *
import dj_database_url

DEBUG = True

INSTALLED_APPS.append('debug_toolbar')

"""
Local Database Settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
"""

# Heroku Database Settings
DATABASES = {
    'default': dj_database_url.config('CLEARDB_DATABASE_URL')
}


SITE_URL = 'art-by-keryn.herokuapp.com'

# PayPal Settings
PAYPAL_NOTIFY_URL = 'art-by-keryn.herokuapp.com/a-very-hard-to-guess-url/'
PAYPAL_RECEIVER_EMAIL = 'nicole-merchant2@gmail.com'
