CONCURRENT_REQUESTS = 32

DOWNLOAD_DELAY = 0.5
CONCURRENT_REQUESTS_PER_DOMAIN = 16
CONCURRENT_REQUESTS_PER_IP = 16

DOWNLOADER_MIDDLEWARES = {
    'rotating_proxies.middlewares.RotatingProxyMiddleware': 610,
    'rotating_proxies.middlewares.BanDetectionMiddleware': 620,
}

ROTATING_PROXY_LIST_PATH = "../proxy.txt"
ROTATING_PROXY_PAGE_RETRY_TIMES = len(open(ROTATING_PROXY_LIST_PATH, 'r').readlines()) / 10

AUTOTHROTTLE_ENABLED = False
AUTOTHROTTLE_START_DELAY = 5
AUTOTHROTTLE_MAX_DELAY = 60
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
AUTOTHROTTLE_DEBUG = False

HTTPCACHE_ENABLED = False
HTTPCACHE_EXPIRATION_SECS = 30
HTTPCACHE_DIR = 'httpcache'
HTTPCACHE_IGNORE_HTTP_CODES = [*range(200, 305)] #[200, 302]
HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

DNSCACHE_ENABLED = True
DNSCACHE_SIZE = 10000
DNS_TIMEOUT = 60

DOWNLOADER_CLIENT_TLS_CIPHERS = 'DEFAULT'
DOWNLOADER_CLIENT_TLS_METHOD = 'TLS'