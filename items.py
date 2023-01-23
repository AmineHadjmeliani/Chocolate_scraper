import scrapy
from scrapy.loader import ItemLoader 
from itemloaders.processors import TakeFirst, MapCompose # import the processors
from w3lib.html import remove_tags # import the function to remove html tags
import re

# function to remove non-numeric characters from the scraped price
def remove_regex(price):
    return re.findall(r'(?:\d+\.)?\d+.\d+', price)

# function to add the domain name to the scraped link
def add_abs_link(link):
    return "chocolate.co.uk"+link


class ChocolateProduct(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field(input_processor = MapCompose(remove_tags), # remove html tags
                        output_processor=TakeFirst()) # take the first non-null value
    price = scrapy.Field(input_processor = MapCompose(remove_regex), # remove non-numeric characters
                        output_processor=TakeFirst()) # take the first non-null value
    link = scrapy.Field(input_processor = MapCompose(add_abs_link), # add the domain name to the link
                        output_processor=TakeFirst()) # take the first non-null value
