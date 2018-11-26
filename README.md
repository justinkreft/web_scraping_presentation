# Robust Web Scraping, (Some) Natural Language Processing, and Startup Culture
***************************************************

*Author*: Justin Kreft
*Email*: justin(dot)kreft(at)quantworks(dot).com

**This** presentation was given to a group of interested students at UNC-CH on 2018-11-27.
The intent of the presentation was a high-level introduction to choices that will enable
robust webscraping techiques. It also demonstrated how to hook some NLP processes into that
webscraping architecture. It focuses on sharing comming methods of parsing web content,
and specifically recommends Scrapy for production web scraping applications.

## Build instructions
==================

Use `make setup` after cloning repo to install dependencies
Use `make start-notebook` to start Jupyter notebook

If wanting to use sample scrapy library cd into
`cd <repo_location>/scraping_nlp_presentation/rotten_tomatoes`
`source .venv/bin/activate`
`scrapy crawl movie_scrape`
