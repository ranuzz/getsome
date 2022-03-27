"""Top-level package for getsome."""

__author__ = """shekhar chandra"""
__email__ = 'ranuzz@outlook.com'
__version__ = '0.1.5'

import logging

from sqlalchemy.ext.declarative import declarative_base
from getsome import configuration

SqlBase = declarative_base()

logging.info('getting config')
AppConfig = configuration.get_config()
logging.info('setting up log')
AppConfig.setup_log()
logging.info('setting up db')
AppConfig.setup_db()
