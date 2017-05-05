import scrapy
from scrapy.loader.processors import TakeFirst
from scrapy.loader import ItemLoader
from scrapy import FormRequest
from scrapy.item import Item, Field
from scrapy.http import Request
import logging

class PlayGroundItem(Item):
    title = Field()
    url = Field()
    download_url = Field()


class PlayGroundLoader(ItemLoader):
    default_output_processor = TakeFirst()


class PlayGroundSpider(scrapy.Spider):
    name = "playground_spider"
    # allowed_domains = ["http://www.playground.ru"]
    # start_urls = ["http://www.playground.ru/files/stalker_clear_sky/"]
    # start_urls = ['https://auth.playground.info/ru/login']

    # allowed_domains = ["http://www.playground.ru", "https://auth.playground.info/ru/login"]
    start_urls = [
        "http://www.playground.ru"
    ]

    def start_requests(self):
        return [Request(url="http://www.playground.ru", callback=self.login)]

    def login(self, response):
        logging.error("1: ")
        logging.error(response.body)
        return scrapy.FormRequest('https://auth.playground.info/ru/login',
                                  headers={"X-Requested-With": "XMLHttpRequest"},
                                  formdata={'_name': 'Ethertrust', '_password': 'STARWARS1',
                                            '_csrf_token': response.xpath(
                                                "//input[@name='_csrf_token']/@value").extract_first()},
                                  callback=self.parse, dont_filter=True)

    def parse(self, response):
        logging.error("2: ")
        logging.error(response.body)
        if "Goutam" in response.body:
            print("Successfully logged in. Let's start crawling!")
        else:
            print("Login unsuccessful")