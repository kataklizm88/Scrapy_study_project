# Scrapy settings for new_project project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "new_project"

SPIDER_MODULES = ["new_project.spiders"]
NEWSPIDER_MODULE = "new_project.spiders"
LOG_ENBLES = True
LOG_LEVEL = 'DEBUG'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)' \
             ' Chrome/108.0.0.0 YaBrowser/23.1.1.1138 Yowser/2.5 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 2

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

IMAGES_STORE = 'files'
# Disable cookies (enabled by default)
COOKIES_ENABLED = True

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#     "Accept-Language": "en",
#     'cookie': 'PHPSESSID=aLIEMw3SO7OWRced4J7Ngd8ZnHjKH4PS; BITRIX_SM_book24_visitor_id=0c584962-c8d4-4eb5-9a17-fa6d5280f198; BITRIX_SM_SALE_UID=1855046841; BITRIX_SM_location_name=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3; BITRIX_SM_location_code=c2deb16a-0330-4f05-821f-1d09c93331e6; BITRIX_SM_location_country=RU; BITRIX_SM_location_coords=%5B%2259.939084%22%2C%2230.315879%22%5D; ssaid=11630210-ba98-11ed-b8c4-699dbdc90e2a; _ga=GA1.2.1759289690.1677939781; _gid=GA1.2.1171231361.1677939781; gdeslon.ru.__arc_domain=gdeslon.ru; gdeslon.ru.user_id=7093a472-ccd1-49a4-9bb8-2af9198ef1e7; tmr_lvid=a3091b3bcdf8538bb724fa71aa5bfd1f; tmr_lvidTS=1677939780905; _ym_uid=1677939781389366752; _ym_d=1677939781; tt_deduplication_cookie=yandex; tt_deduplication_cookie=yandex; st_uid=839570063df3ebf9b4216354b7c4e3d5; _tt_enable_cookie=1; _ttp=eduN6s8p0k4nCHM9Ww1JjRSr6js; popmechanic_sbjs_migrations=popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1; analytic_id=1677939781387; flocktory-uuid=0948e288-dc69-4531-87c8-8db3334c3c0c-7; adid=167793978227934; BITRIX_SM_location_accept=Y; BITRIX_SM_location_region_code=c2deb16a-0330-4f05-821f-1d09c93331e6; COOKIES_ACCEPTED=Y; g4c_x=1; _ym_isad=2; _ym_visorc=b; tmr_detect=0%7C1678015467901; mindboxDeviceUUID=c152be95-8499-4ed2-ac8e-19ffb1ed32f9; directCrm-session=%7B%22deviceGuid%22%3A%22c152be95-8499-4ed2-ac8e-19ffb1ed32f9%22%7D; __tld__=null'
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "new_project.middlewares.NewProjectSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    "new_project.middlewares.NewProjectDownloaderMiddleware": 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   "new_project.pipelines.NewProjectPipeline": 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
