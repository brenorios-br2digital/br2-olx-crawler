# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Olxcrawler2Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class IphoneOfferItem(scrapy.Item):
    product_id = scrapy.Field()
    url = scrapy.Field()
    title = scrapy.Field()
    model = scrapy.Field()
    price = scrapy.Field()
    city = scrapy.Field()
    state = scrapy.Field()
    post_date = scrapy.Field()
    post_time = scrapy.Field()
    thumb_url = scrapy.Field()
    is_featured = scrapy.Field()
    list_position = scrapy.Field()
    vehicle_report_enabled = scrapy.Field()
    last_bump_age_secs = scrapy.Field()
    olx_pay_enabled = scrapy.Field()
    olx_delivery_enabled = scrapy.Field()

    description = scrapy.Field()
    zipcode = scrapy.Field()
    neighbourhood = scrapy.Field()
    seller_user = scrapy.Field()
    seller_join_date = scrapy.Field()
    seller_phone_verified = scrapy.Field()
    seller_email_verified = scrapy.Field()
    seller_facebook_verified = scrapy.Field()
