from scrapy.crawler import CrawlerProcess
import scrapy
import logging

from scrapy.http import Request

class FirstSpider(scrapy.Spider):
    name = "first"
    allowed_domains = ["instacart.com"]
    start_urls = [
        "https://www.instacart.com"
    ]

    def start_requests(self):
        return [Request(url="https://www.instacart.com", callback=self.login)]

    def login(self, response):
        return scrapy.FormRequest('https://www.instacart.com/accounts/login',
                                  headers={"X-Requested-With": "XMLHttpRequest"},
                                  formdata={'user[email]': 'egoshvedo@mail.ru', 'user[password]': 'STARWARS1',
                                            "authenticity_token": response.xpath(
                                                "//meta[@name='csrf-token']/@content").extract_first()},
                                  callback=self.parse,dont_filter=True)

    def parse(self, response):
        logging.error(response.body)
        if "Goutam" in response.body:
            print("Successfully logged in. Let's start crawling!")
        else:
            print("Login unsuccessful")