# Chocolate_scraper

This tutorial is for those new to Scrapy and aims to provide a comprehensive guide on how to create your first spider project using Python3. It covers the basics of crawling with a basic spider and walks you through building a complete tutorial project, including exporting the data to a CSV file. The tutorial will teach you how to scrape product names and prices from an online shop and also how to use the Scrapy shell to parse data, extract text and href attributes from HTML, and scrape multiple pages.


This is a Python script using the Scrapy library to scrape data from the website chocolate.co.uk. The script defines a class ChocolateSpider which is a subclass of scrapy.Spider. The spider has a name '`chocolate`', allowed_domains of ['chocolate.co.uk'] and start_urls of ['https://www.chocolate.co.uk/collections/all'].

In the parse method, the script uses the css selector to extract the list of products from the HTML response. It iterates through each product and for each product, it creates an ItemLoader object named "il" with an instance of the custom class `ChocolateProduct()` as the item and the current product as the selector.

Then, it uses the add_css method to extract the following information from the current product:

name: the text of the 'div.product-item__info a' element
price: the text of the 'span.price' element
link: the value of the 'href' attribute of the 'div.product-item-meta a' element
Finally, it yields the loaded item using `il.load_item()` method.

This script is scraping the name, price and link of the chocolate products from the website `chocolate.co.uk` using the css selectors and loading the scraped data in the ChocolateProduct object.

The script also has the functionality to scrape multiple pages by selecting the next page using the css selector "[rel=next]" and using `response.follow()` method. The script will keep on scraping the next page until there is no next page available.
