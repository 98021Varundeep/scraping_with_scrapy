# Scrapy settings for ZillowScraping project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "ZillowScraping"

SPIDER_MODULES = ["ZillowScraping.spiders"]
NEWSPIDER_MODULE = "ZillowScraping.spiders"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "ZillowScraping (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 1

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    # 'cookie': 'zguid=24|%245fabd5d9-30fd-4d2a-9b10-197d39ebf997; zgsession=1|7f0a829f-2a15-4594-a758-e189309700a4; _ga=GA1.2.504499196.1725446786; _gid=GA1.2.1790322492.1725446786; zjs_anonymous_id=%225fabd5d9-30fd-4d2a-9b10-197d39ebf997%22; zjs_user_id=null; zg_anonymous_id=%22aecfa6f3-820b-47a5-a7ca-695f50a29669%22; pxcts=ef22249d-6aaa-11ef-b3c8-8004b6cc366e; _pxvid=ef221026-6aaa-11ef-b3c8-9295ee71bb8c; _gcl_au=1.1.657603840.1725446788; DoubleClickSession=true; _tt_enable_cookie=1; _ttp=D6cIPSx06v2WQX-JjwJAVYVgVK6; _fbp=fb.1.1725446789119.774670539722507697; _pin_unauth=dWlkPVltUmlNakZtWTJJdE9ETmlaUzAwTW1ZeExUazJPRGt0TnpRNE9Ua3pOVE5sTkRkbQ; _clck=ualoyp%7C2%7Cfow%7C0%7C1708; _scid=a3db2b8c-2a7c-4d36-a606-0d6f4166dd85; _ScCbts=%5B%22299%3Bchrome.2%3A2%3A5%22%2C%22321%3Bchrome.2%3A2%3A5%22%5D; _sctr=1%7C1725388200000; JSESSIONID=C21E909F77E30128D61B4929CB670A38; _rdt_uuid=1725446788808.6f406b8f-2c56-4c2c-81e6-84ce734a3a46; _scid_r=a3db2b8c-2a7c-4d36-a606-0d6f4166dd85; AWSALB=RopTR9BV1vbJ1iqJECrMDxdZKyDAvVuE2RGCL1uw/j2N0QZlabDpnltQVvFOfH1j73jzQgzFKKCAdPvrfn84h0AWtGFOFxmS4N2mJhJAcQtU1UZNW+/xpx0S6HLH; AWSALBCORS=RopTR9BV1vbJ1iqJECrMDxdZKyDAvVuE2RGCL1uw/j2N0QZlabDpnltQVvFOfH1j73jzQgzFKKCAdPvrfn84h0AWtGFOFxmS4N2mJhJAcQtU1UZNW+/xpx0S6HLH; _uetsid=f0f4bfd06aaa11ef82432b0e97ff94ab; _uetvid=f0f4f7806aaa11ef9c49bbcf0f8684c7; _derived_epik=dj0yJnU9WVF2Zkxyci1rbjdSQVRPb1E5Tm1jQThiRHNkVVhRZ3Mmbj1fRlVBcnpSVnNRYU9jWjRWYy00emtRJm09MSZ0PUFBQUFBR2JZU2pRJnJtPTEmcnQ9QUFBQUFHYllTalEmc3A9Mg; _px3=77c23bc2696c18d0218a623f2e2da999d94a43c2e8093f45e77e2be166377374:+IgpXuHEykFtqWfaHVPxjDny+KhZozeHRovvBeJTzVyd07JGvY5zbk9GC0DMH6+JNxdRrjSS2+MvciBqHYPIiA==:1000:ofczE2ed4KSRz0HtTdgDV/cdjixl2Rb8AV9Iwg48Ag0TilU0eIVHI1sZwDV5Mn+y6bww+VeuIZ2wkDT+JxpI5ZEXRYpm+/Z6Api3yxfb+VQ34g5z7w3YoTWSYFsq4dimxqIqqqKZbJYyaskMhOMtIDBcYTVCtylnGgrBgt6lt5t1FyVGh/ss7WhxixUgOMCDy/Flg7+rpDJd8eK0E7XdmcluecvePuiIXUcQGKuShkY=; search=6|1728044258969%7Crect%3D41.02915720380264%2C-73.3960323183594%2C40.36489002052367%2C-74.56332968164065%26rid%3D6181%26disp%3Dmap%26mdm%3Dauto%26p%3D1%26z%3D1%26listPriceActive%3D1%26fs%3D1%26fr%3D0%26mmm%3D0%26rs%3D0%26ah%3D0%26singlestory%3D0%26housing-connector%3D0%26parking-spots%3Dnull-%26abo%3D0%26garage%3D0%26pool%3D0%26ac%3D0%26waterfront%3D0%26finished%3D0%26unfinished%3D0%26cityview%3D0%26mountainview%3D0%26parkview%3D0%26waterview%3D0%26hoadata%3D1%26zillow-owned%3D0%263dhome%3D0%26featuredMultiFamilyBuilding%3D0%26student-housing%3D0%26income-restricted-housing%3D0%26military-housing%3D0%26disabled-housing%3D0%26senior-housing%3D0%26commuteMode%3Ddriving%26commuteTimeOfDay%3Dnow%09%096181%09%7B%22isList%22%3Atrue%2C%22isMap%22%3Afalse%7D%09%09%09%09%09; _clsk=1ua8xm8%7C1725452259720%7C5%7C0%7Cs.clarity.ms%2Fcollect',
    'priority': 'u=0, i',
    'referer': 'https://www.zillow.com/',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
}
  


# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "ZillowScraping.middlewares.ZillowscrapingSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    "ZillowScraping.middlewares.ZillowscrapingDownloaderMiddleware": 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    "ZillowScraping.pipelines.ZillowscrapingPipeline": 300,
#}

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
