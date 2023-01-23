import scrapy
from scrapy.loader import ItemLoader
from ..items import ChocolateProduct

 
class ChocolateSpider(scrapy.Spider):
    name = 'chocolate'
    allowed_domains = ['chocolate.co.uk']
    start_urls = ['https://www.chocolate.co.uk/collections/all']

    # This is the main method that gets called by Scrapy when the spider starts
    def parse(self, response):
        
        # Use the CSS selector to extract all the product elements from the HTML response
        products = response.css("product-item.product-item")
        for product in products:
            
            ## the sophisticated method
            # Create an ItemLoader object with an instance of the custom class ChocolateProduct
            il = ItemLoader(item=ChocolateProduct(), response=response, selector=product)
            # Use the add_css method to extract the name of the product
            il.add_css('name', 'div.product-item__info a') 
            # Use the add_css method to extract the price of the product
            il.add_css('price', 'span.price') 
            # Use the add_css method to extract the link of the product
            il.add_css('link',  'div.product-item-meta a::attr(href)')
            # Yield the loaded item
            yield il.load_item()
            
            '''The second method '''
            # il = ChocolateProduct()
            # il['name'] = p.css("div.product-item__info a::text").get()
            # il['price'] =  re.findall(r'£(?:\d+\.)?\d+.\d+', p.css("span.price").get())
            # il['link'] = response.follow(p.css('div.product-item-meta a').attrib['href'])
            # yield il 
            
            '''The basic method'''
            # yield {
            # 'name': p.css("div.product-item__info a::text").get(),
            
            # 'price': re.findall(r'£(?:\d+\.)?\d+.\d+', p.css("span.price").get()),
            # 'link': response.follow(p.css('div.product-item-meta a').attrib['href'])
            # }
        
        # Select the next page if exists 
        next_page = response.css('[rel=next]').attrib['href']
        if next_page:
            # Follow the next page using the response.follow() method
            yield response.follow(next_page, callback = self.parse)
