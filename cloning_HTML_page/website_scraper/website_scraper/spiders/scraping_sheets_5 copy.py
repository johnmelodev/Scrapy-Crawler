import scrapy


class ProxyScraperSpider(scrapy.Spider):
    # identity
    name = 'sheetsbot'

    # Request
    def start_requests(self):
        urls = ['https://us-proxy.org']

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    # Response
    def parse(self, response):
        # Path of the table.
        for line in response.xpath("//table[@class='table table-striped table-bordered']//tr"):
            # Path of the lines.
            yield {
                'IP Address': line.xpath('./td[1]/text()').get(),
                'Port': line.xpath('./td[2]/text()').get(),
                'Code': line.xpath('./td[3]/text()').get(),
                'Country': line.xpath('./td[4]/text()').get(),
                'Anonymity': line.xpath('./td[5]/text()').get(),
                'Google1': line.xpath('./td[6]/text()').get(),
                'Google2': line.xpath('./td[7]/text()').get(),
                'Last Checked': line.xpath('./td[8]/text()').get()
            }
