import os

DEBUG = True

TEMPLATE_DEBUG = DEBUG

PROJECT_HOME = os.getcwd()

APP_NAME = PROJECT_HOME[PROJECT_HOME.rindex(os.sep)+1:]

ADMINS = (

    # ('Your Name', 'your_email@domain.com'),

)
