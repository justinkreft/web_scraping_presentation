# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MovieItem(scrapy.Item):

    id = scrapy.Field()
    url = scrapy.Field()
    title = scrapy.Field()
    synopsis = scrapy.Field()
    tomatoIcon = scrapy.Field()
    tomatoScore = scrapy.Field()
    popcornIcon = scrapy.Field()
    popcornScore = scrapy.Field()
    text_blob = scrapy.Field()
    vector = scrapy.Field()
