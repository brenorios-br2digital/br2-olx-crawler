# -*- coding: utf-8 -*-
import scrapy

from olxcrawler2.utils.utils import XPATH_FEATURES
from ..items import IphoneOfferItem
from datetime import datetime, timedelta


class IphoneoffersSpider(scrapy.Spider):
    name = 'iphoneoffers'
    allowed_domains = ['http://www.olx.com.br/', 'olx.com.br']
    start_urls = ['https://www.olx.com.br/brasil?q=iphone']

    def parse(self, response):
        offerItem = IphoneOfferItem()
        offerList = response.xpath(XPATH_FEATURES["list"])
        
        for offer in offerList: 
            offerItem["product_id"] = offer.xpath(XPATH_FEATURES["product_id"]).get()
            detail_url = offer.xpath(XPATH_FEATURES["url"]).get()
            offerItem["url"] = detail_url
            offerItem["title"] = offer.xpath(XPATH_FEATURES["title"]).get()
            offerItem["price"] = offer.xpath(XPATH_FEATURES["price"]).get()
            offerItem["post_time"] = offer.xpath(XPATH_FEATURES["post_time"]).get()
            offerItem["city"] = offer.xpath(XPATH_FEATURES["city"]).get()
            offerItem["thumb_url"] = offer.xpath(XPATH_FEATURES["thumb_url"]).get()
            offerItem["is_featured"] = offer.xpath(XPATH_FEATURES["is_featured"]).get()
            offerItem["list_position"] = offer.xpath(XPATH_FEATURES["list_position"]).get()
            offerItem["vehicle_report_enabled"] = offer.xpath(XPATH_FEATURES["vehicle_report_enabled"]).get()
            offerItem["last_bump_age_secs"] = offer.xpath(XPATH_FEATURES["last_bump_age_secs"]).get()
            offerItem["olx_pay_enabled"] = offer.xpath(XPATH_FEATURES["olx_pay_enabled"]).get()
            offerItem["olx_delivery_enabled"] = offer.xpath(XPATH_FEATURES["olx_delivery_enabled"]).get()

            # if detail_url is not None:
            #     print("url is not none", flush=True)
            #     detail_req = scrapy.Request(url=detail_url, callback=self.parse_details)
            #     detail_req.meta['item'] = offerItem

            #     yield detail_req

            yield offerItem

            nextPageUrl = response.xpath(XPATH_FEATURES["next_page"]).get()
            if nextPageUrl is not '' and nextPageUrl is not None:
                if 'o=' in nextPageUrl:
                    pageNum = nextPageUrl.split('o=')[1].split('&')[0]
                    print(f'Current page: {pageNum}')
                else:
                    print(f'Current page: 1')
                yield response.follow(url=nextPageUrl, callback=self.parse)  

    def parse_details(self, response):
        item = response.meta['item']
        item["description"] = response.xpath(XPATH_FEATURES["description"]).get()
        item["zipcode"] = response.xpath(XPATH_FEATURES["zipcode"]).get()
        item["neighbourhood"] = response.xpath(XPATH_FEATURES["neighbourhood"]).get()
        item["seller_user"] = response.xpath(XPATH_FEATURES["seller_user"]).get()
        item["seller_join_date"] = response.xpath(XPATH_FEATURES["seller_join_date"]).get()
        item["seller_phone_verified"] = response.xpath(XPATH_FEATURES["seller_phone_verified"]).get()
        item["seller_email_verified"] = response.xpath(XPATH_FEATURES["seller_email_verified"]).get()
        item["seller_facebook_verified"] = response.xpath(XPATH_FEATURES["seller_facebook_verified"]).get()
        
        yield item

        

        


    

    

