# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from datetime import datetime, timedelta
from .utils.utils import IPHONE_MODELS_LIST

class Olxcrawler2Pipeline:
    def process_item(self, item, spider):
        return item

class IphoneOfferPipeline:
    def process_item(self, offerItem, spider):
        if offerItem['post_time'] is not None and ',' in offerItem['post_time']:
            offerItem["post_date"] = self.getDate(offerItem["post_time"].split(',')[0])
            offerItem["post_time"] = offerItem["post_time"].split(',')[1].strip()

        if offerItem["price"] is not None:
            offerItem["price"] = float(offerItem["price"].replace("R$", "").strip().replace('.', ''))
            
            
        offerItem["is_featured"] = True if offerItem['is_featured'] == '1' else False
        offerItem["list_position"] = int(offerItem['list_position'])

        if offerItem["city"] is not None and offerItem["city"] != '':
                offerItem["state"] = offerItem["city"].split(' - ')[1].strip()
                offerItem["city"] = offerItem["city"].split(' - ')[0].strip()
        else:
            offerItem["city"] = None
            offerItem["state"] = None

        offerItem["vehicle_report_enabled"] = True if offerItem['vehicle_report_enabled'] == 'true' else False
        offerItem["olx_pay_enabled"] = True if offerItem['olx_pay_enabled'] == 'true' else False
        offerItem["olx_delivery_enabled"] = True if offerItem['olx_delivery_enabled'] == 'true' else False
        offerItem["last_bump_age_secs"] = int(offerItem['last_bump_age_secs'])
        # offerItem["seller_phone_verified"] = True if 'não' not in offerItem['seller_phone_verified'] else False
        # offerItem["seller_email_verified"] = True if 'não' not in offerItem['seller_email_verified'] else False
        # offerItem["seller_facebook_verified"] = True if 'não' not in offerItem['seller_facebook_verified'] else False

        return offerItem

    def getModel(self, title):
        for model in  IPHONE_MODELS_LIST:
            if model in title:
                return model
            else:
                return None

    def getDate(self, date):
        if date == 'Hoje':
            return datetime.now().strftime('%Y-%m-%d')
        elif date == 'Ontem':
            return (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
        else:
            return datetime.now().strftime('%Y-') + datetime.strptime(date, '%d/%m').strftime('%m-%d')        

    def formatDate(self, date):
        if date == 'fev':
            return date.replace('fev', 'feb')
        elif date == 'abr':
            return date.replace('abr', 'apr')
        elif date == 'mai':
            return date.replace('mai', 'may')
        elif date == 'ago':
            return date.replace('ago', 'aug')
        elif date == 'set':
            return date.replace('set', 'sep')
        elif date == 'out':
            return date.replace('out', 'oct')
        elif date == 'dez':
            return date.replace('dez', 'dec')
