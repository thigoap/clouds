AUTHOR = 'thigoap'
SITENAME = 'Cloud'
SITEURL = 'https://thigoap.github.io/clouds'

PATH = 'content'
STATIC_PATHS = ['images']

TIMEZONE = 'America/Araguaina'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False
DELETE_OUTPUT_DIRECTORY = True
OUTPUT_PATH = 'docs/'
# THEME = 'notmyidea'
THEME = "./theme/mnml"


USE_FOLDER_AS_CATEGORY = True