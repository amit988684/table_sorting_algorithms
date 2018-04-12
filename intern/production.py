from .settings import *

import dj_database_url

ENVIRONMENT = 'production'
DEBUG = False
ALLOWED_HOSTS = ['']
DATABASES['default'] = dj_database_url.config(
    default='postgres://fpxptcwyrfrxbk:d4a8b92013c9ea2532fa5e2881400a7c3aa1cf32a158865e44bff19e55b5c541@ec2-23-23-142-5.compute-1.amazonaws.com:5432/dc1biu8dtum5gp'
)
