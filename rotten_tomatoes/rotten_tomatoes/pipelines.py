# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import html
import re

import spacy


class MovieCleaningPipeline(object):
    def process_item(self, item, spider):
        for field in item:
            if type(item[field]) == str:
                item[field] = self.clean_text(item[field])

        return item

    def clean_text(self, text):
        re_tags = re.compile(r'<([^>]+)>', re.UNICODE)
        out_text = re_tags.sub('', text)
        if out_text == '':
            out_text = None
        out_text = html.unescape(out_text)
        out_text = out_text.strip()

        return out_text


class MovieNLPPipeline(object):
    def __init__(self):
        self.nlp = spacy.load('en_core_web_md')

    def process_item(self, item, spider):
        item['vector'] = self.nlp(item['text_blob']).vector
        return item


class MovieStoragePipeline(object):
    def process_item(self, item, spider):
        # Add item logic for item persistance. (i.e. save to disk, or insert into database)
        return item
