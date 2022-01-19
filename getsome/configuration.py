import os
import sys
import configparser
from pathlib import Path
import logging
from sqlalchemy import create_engine
import datetime


class AppConfig:
    app_home = None
    config_path = None
    instance_name = None
    rss_feed_path = None

    # logging
    abs_log_folder = None

    base_log_folder = None
    log_file_pattern = None
    logging_level = None
    log_format = None
    simple_log_format = None

    # database
    db_engine = None

    sql_alchemy_conn = None

    def setup_log(self):
        self.abs_log_folder = os.path.join(self.app_home, self.base_log_folder)
        os.makedirs(self.abs_log_folder, exist_ok=True)
        log_file = os.path.join(
            self.abs_log_folder,
            "getsome.log")
        #datetime.datetime.now().strftime(self.log_file_pattern) + ".log")
        logging.basicConfig(
            filename=log_file,
            stream=sys.stdout,
            filemode='w+',
            format='%(asctime)s - %(levelname)s:%(message)s',
            level=logging.DEBUG
        )

    def setup_db(self):
        self.db_engine = create_engine(self.sql_alchemy_conn)


def _read_default_file(file_name):
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    with open(file_path, encoding='utf-8') as default_file:
        return default_file.read()


def get_app_home():
    app_home = os.path.join(str(Path.home()), '.getsome_config')
    if not os.path.exists(app_home):
        os.makedirs(app_home, exist_ok=True)
    return app_home


def get_config_path(app_home):
    config_path = os.path.join(app_home, 'getsome.cfg')
    if not os.path.exists(config_path):
        logging.info("Creating config file in {0}".format(app_home))
        default_config = _read_default_file('getsome.cfg')
        with open(config_path, 'w') as fp:
            fp.write(default_config)
    if not os.path.isfile(config_path):
        raise OSError("Invalid config path {0}".format(config_path))
    return config_path


def get_rss_feed_path(app_home):
    rss_feed_path = os.path.join(app_home, 'feeds.txt')
    if not os.path.exists(rss_feed_path):
        logging.info("Creating rss feed file in {0}".format(app_home))
        default_file = _read_default_file('feeds.txt')
        with open(rss_feed_path, 'w') as fp:
            fp.write(default_file)
    if not os.path.isfile(rss_feed_path):
        raise OSError("Invalid config path {0}".format(rss_feed_path))
    return rss_feed_path


def get_config():
    app_home = get_app_home()
    config_path = get_config_path(app_home)
    rss_feed_path = get_rss_feed_path(app_home)
    config = configparser.ConfigParser()
    config.read(config_path)
    app_config = AppConfig()

    # app
    app_config.app_home = app_home
    app_config.config_path = config_path
    app_config.rss_feed_path = rss_feed_path
    app_config.instance_name = config['getsome']['instance_name']

    # logging
    log_config = config['logging']
    app_config.log_format = log_config['log_format']
    app_config.base_log_folder = log_config['base_log_folder']
    app_config.logging_level = log_config['logging_level']
    app_config.simple_log_format = log_config['simple_log_format']
    app_config.log_file_pattern = log_config['log_file_pattern']

    # database
    db_config = config['database']
    app_config.sql_alchemy_conn = db_config['sql_alchemy_conn']
    if app_config.sql_alchemy_conn == 'sqlite:////getsome.db':
        app_config.sql_alchemy_conn = 'sqlite:///{0}/getsome.db'.format(
            app_config.app_home)

    return app_config
