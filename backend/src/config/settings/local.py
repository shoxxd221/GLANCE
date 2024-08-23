from .base import *


DEBUG = True

THIRD_PARTY_APPS += 'debug_toolbar'

MIDDLEWARE += 'debug_toolbar.middleware.DebugToolbarMiddleware'

INTERNAL_IPS = [
    '172.19.0.1',
]
