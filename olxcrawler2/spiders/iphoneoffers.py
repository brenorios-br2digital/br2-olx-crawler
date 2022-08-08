# -*- coding: utf-8 -*-
import scrapy

from olxcrawler2.utils.utils import XPATH_FEATURES
from ..items import IphoneOfferItem
from datetime import datetime, timedelta


class IphoneoffersSpider(scrapy.Spider):
    name = 'iphoneoffers'
    allowed_domains = ['http://www.olx.com.br/', 'www.olx.com.br']
    start_urls = ['http://www.olx.com.br/celulares/iphone/usado?q=iphone/']

    def parse(self, response):
        offerItem = IphoneOfferItem()
        offerList = response.xpath(XPATH_FEATURES["list"])
        
        for offer in offerList: 
            offerItem["product_id"] = offer.xpath(XPATH_FEATURES["product_id"]).get()
            offerItem["url"] = offer.xpath(XPATH_FEATURES["url"]).get()
            offerItem["title"] = offer.xpath(XPATH_FEATURES["title"]).get()
            offerItem["price"] = offer.xpath(XPATH_FEATURES["price"]).get()
            offerItem["post_time"] = offer.xpath(XPATH_FEATURES["post_time"]).get()
            offerItem["city"] = offer.xpath(XPATH_FEATURES["city"]).get()
            offerItem["thumb_url"] = offer.xpath(XPATH_FEATURES["thumb_url"]).get()
            offerItem["is_featured"] = offer.xpath(XPATH_FEATURES["is_featured"]).get()
            offerItem["list_position"] = offer.xpath(XPATH_FEATURES["list_position"]).get()
            

            yield offerItem

        nextPageUrl = response.xpath().get(XPATH_FEATURES["next_page"])
        if nextPageUrl is not '' and nextPageUrl is not None:
            if 'o=' in nextPageUrl:
                pageNum = nextPageUrl.split('o=')[1].split('&')[0]
                print(f'Current page: {pageNum}')
            else:
                print(f'Current page: 1')
            yield response.follow(url=nextPageUrl, callback=self.parse)   


    

    

