# Use this website as an example: https://quotes.toscrape.com
# Type on terminal: scrapy startproject name_of_project
# Example: scrapy startproject website_scraper
# Create a spider (a .py file inside /website_scraper/spiders)

import scrapy
# CamelCase (each new word should start with a capital letter)
# Create a class with a name related to what you are going to scrape and append Spider at the end for good practices


class QuotesToScrapeSpider(scrapy.Spider):
    # Identity
    name = 'quotebot'
    # Request

    def start_requests(self):
        # Define URLs to scrap
        urls = ['https://quotes.toscrape.com/']

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    # Response
    def parse(self, response):
        # Here is where you should process what is returned from the response
        with open('html.page', 'wb') as file:
            file.write(response.body)

# in order to make it work and scrapy the website. we should use the terminal. cd should be in the folder and then scrapy crawl quotebot

# scrapy crawl quotebot