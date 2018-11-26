# -*- coding: utf-8 -*-

BOT_NAME = 'rotten_tomatoes'
LOG_LEVEL = "DEBUG"
SPIDER_MODULES = ['rotten_tomatoes.spiders']
NEWSPIDER_MODULE = 'rotten_tomatoes.spiders'

# Configure middlewares. All of these are recommended
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.robotstxt.RobotsTxtMiddleware': 100,
    'scrapy.downloadermiddlewares.downloadtimeout.DownloadTimeoutMiddleware': 350,
    'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware': 400,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': 500,
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': 550,
    'scrapy.downloadermiddlewares.ajaxcrawl.AjaxCrawlMiddleware': 560,
    'scrapy.downloadermiddlewares.redirect.MetaRefreshMiddleware': 580,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 590,
    'scrapy.downloadermiddlewares.redirect.RedirectMiddleware': 600,
    'scrapy.downloadermiddlewares.cookies.CookiesMiddleware': 700,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
    'scrapy.downloadermiddlewares.stats.DownloaderStats': 850,
    'scrapy.downloadermiddlewares.httpcache.HttpCacheMiddleware': 900,
    # advised to use proxy middle ware as well
}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'rotten_tomatoes.pipelines.MovieCleaningPipeline': 100,
    'rotten_tomatoes.pipelines.MovieNLPPipeline': 110,
    'rotten_tomatoes.pipelines.MovieStoragePipeline': 120,
}

# These are typical settings for a generic project.
# Read docs at https://doc.scrapy.org/en/latest/topics/settings.html?highlight=settings
ROBOTSTXT_OBEY = True
DOWNLOADER_STATS = True
COOKIES_DEBUG = False
AUTOTHROTTLE_ENABLED = True
DOWNLOAD_TIMEOUT = 60
CONCURRENT_REQUESTS = 16
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.87 Safari/537.36'
