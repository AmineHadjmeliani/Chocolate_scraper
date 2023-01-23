# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy import Spider
from scrapy.exceptions import DropItem



class ChocolatespiderPipeline:
    def process_item(self, item, spider):
        return item


class PriceToUSDPipeline:
    rate = 1.1
    def process_item(self,item, spider):
        adapter = ItemAdapter(item)
        
        if adapter.get('price'):
            floatprice = float(adapter['price'])
            adapter['price']= round(floatprice*self.rate, 2)
            return item
        else :
            raise DropItem(f'missing price in {item}')
        
class DuplicatePipeline:
    def __init__(self):
        self.name__seen = set()
        
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if adapter['name'] in self.name__seen:
            raise DropItem(f"Duplicate item found: {item}")
        else:
            self.name__seen.add(adapter['name'])
            return item
            
    
            
            
# class SavingToPostgresPipeline:
#     def __init__(self) -> None:
#         self.create_connection()
        
#     def create_connection(self):
#         self.conn = psycopg2.connect(
#                                     host = 'localhost',
#                                     database = 'chocolate_scraping', 
#                                     user = 'root', 
#                                     password= '12345678')
#         self.cr = self.connection.cursor()
    