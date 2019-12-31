# -*- coding: utf-8 -*-

# Scrapy settings for {{cookiecutter.project_name}} project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import os

import yaml
from prettyconf import config
from scrapy.utils.log import configure_logging

# Setup the environment
DEBUG = config('DEBUG', cast=config.boolean)

# MongoDB setup
MONGODB_CONN_URI = config('MONGODB_CONN_URI')
MONGODB_DB_HOST = config('MONGODB_DB_HOST')
MONGODB_DB_PORT = config('MONGODB_DB_PORT')
MONGODB_DB_NAME = config('MONGODB_DB_NAME')
MONGODB_DB_USER = config('MONGODB_DB_USER')
MONGODB_DB_PASS = config('MONGODB_DB_PASS')

# Logging setup
logger_path = os.path.join(os.path.dirname(__file__), '../logger.yaml')

with open(logger_path, 'r') as file:
    logger_config = yaml.safe_load(file.read())
    configure_logging(logger_config, False)

LOG_ENABLED = True
LOG_LEVEL = 'development' if DEBUG else 'production'

BOT_NAME = '{{cookiecutter.project_slug}}'

SPIDER_MODULES = ['{{cookiecutter.project_slug}}.spiders']
NEWSPIDER_MODULE = '{{cookiecutter.project_slug}}.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
              '(KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36')

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    '{{cookiecutter.project_slug}}.middlewares.{{cookiecutter.scrapy.project_main_class}}SpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    '{{cookiecutter.project_slug}}.middlewares.{{cookiecutter.scrapy.project_main_class}}DownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    '{{cookiecutter.project_slug}}.pipelines.{{cookiecutter.scrapy.project_main_class}}Pipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True
# The initial download delay
AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'