#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Hamish Cunningham'
SITENAME = u'WeGrow WaterElf: Local Food, Global Community'
WEGROW_TAGLINE = u'Local Food, Global Community'
SITEURL = ''
PATH = 'content'
TIMEZONE = 'Europe/London'
DEFAULT_LANG = u'en'
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
DEFAULT_PAGINATION = 10

MARKUP = ('rst', 'md', 'html')
IGNORE_FILES=[ '*.mkd', '*.jinja' ]
STATIC_PATHS = ['images', 'pages/images', '.htaccess', '.htpasswd']
FILENAME_METADATA = ('(?P<date>\d{4}-\d{2}-\d{2}).*')
PAGE_EXCLUDES = ([])
ARTICLE_EXCLUDES = (['pages'])
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/index.html'
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
SHOW_ARTICLE_AUTHOR = True
MENUITEMS = (
  ( 'About', "/pages/about.html" ),
  ( 'Contact', "/pages/contact.html" ),
)

#THEME = 'theming/original'
THEME='theming/pelican-bootstrap3'
BOOTSTRAP_THEME='united'
#BOOTSTRAP_THEME='cyborg'
#BOOTSTRAP_THEME='darkly'
#BOOTSTRAP_THEME='readable'
#BOOTSTRAP_THEME='cerulean'
#BOOTSTRAP_THEME='superhero'
FAVICON='favicon.ico'
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_TAGS_ON_SIDEBAR = False
DISPLAY_ARTICLE_INFO_ON_INDEX = False
HIDE_SITENAME = True
ARTICLE_ORDER_BY = 'reversed-date'
TWITTER_USERNAME = 'hcunningham'
GOOGLE_ANALYTICS = 'TODO UA-41812045-2'
DISQUS_SITENAME = 'wegrow'
DISQUS_DOMAIN = 'https://wegrow.social'
