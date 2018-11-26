import json
import logging

from scrapy import Spider
from scrapy.http.request import Request

from ..items import MovieItem


class MovieSpider(Spider):

    name = "movie_scrape"
    allowed_domains = ["www.rottentomatoes.com"]
    custom_settings = {}  # Add custom settings for a specific spider in this object
    start_urls = ["https://www.rottentomatoes.com/api/private/v2.0/browse?maxTomato=100&maxPopcorn=100&services=amazon%3Bhbo_go%3Bitunes%3Bnetflix_iw%3Bvudu%3Bamazon_prime%3Bfandango_now&certified&sortBy=release&type=dvd-streaming-all&page=1"]
    # Note that some website track cookies to API calls. If so, you need get a
    # successful request to the parent webpage and maintain cookies
    # (scrapy does by default)

    def parse(self, response):

        json_data = json.loads(response.text)
        # check if this is the first page. Get total records, yield other page requests
        if response.url[-2:] == '=1':
            total_products = json_data["counts"]["total"]
            current_offset = json_data["counts"]["count"]
            pages = (total_products // current_offset) + 1
            while pages > 1:
                # don't filter is set to true to ensure that duplicate requests of the form
                # https://www.rottentomatoes.com/api/private/v2.0/browse are not ignored
                yield Request(response.url[:-1] + str(pages), callback=self.parse, dont_filter=True)
                pages -= 1

        for movie in json_data['results']:  # array of objects
            item = MovieItem()
            try:
                item['id'] = movie['id']
                item['url'] = movie['url']
                item['title'] = movie['title']
                item['synopsis'] = movie['synopsis']
                item['tomatoIcon'] = movie['tomatoIcon']
                item['tomatoScore'] = movie['tomatoScore']
                item['popcornIcon'] = movie['popcornIcon']
                item['popcornScore'] = movie['popcornScore']
            except Exception as e:
                logging.critical('Failed to extract expected field. Site may have changed on {0}. {1}'.format(response.url, e))

            yield Request("https://www.rottentomatoes.com" + item['url'],
                          callback=self.parse_movie_page,
                          dont_filter=True, meta={"item": item})

    def parse_movie_page(self, response):
        item = response.meta['item']

        # while in a production spider, we would probably extract all the fields granularly.
        # This is an example of getting a text blob for subsequent NLP processing
        try:
            item['text_blob'] = response.xpath('//section[contains(@class, "movie_info")]//text()').extract()
            item['text_blob'] = ' '.join([x.strip() for x in item['text_blob'] if x.strip()])
        except Exception as e:
            logging.critical('Failed to extract field on {0}. Site may have changed. {1}'.format(response.url, e))

        yield item
