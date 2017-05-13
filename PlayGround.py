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
        "https://auth.playground.info/ru/login"
    ]

    def start_requests(self):
        return [Request(url="https://auth.playground.info/ru/login", callback=self.login, dont_filter=True)]

    def login(self, response):
        logging.error("1: ")
        logging.error(response.body.decode("utf-8").encode('cp1251'))
        urlname = response.url.replace("/", ".") + '.php'
        urlname = urlname.replace(":", "")
        f = open(urlname, 'w', encoding='utf-8')
        f.write(response.body.decode("utf-8").encode('cp1251').decode('cp1251'))
        return scrapy.FormRequest.from_response(response,
                                  headers={"Content-Type": "application/x-www-form-urlencoded"},
                                  formdata={'_name': 'Ethertrust', '_password': 'STARWARS1'},
                                  callback=self.parse, dont_filter=True)

    def parse(self, response):
        logging.error("2: ")
        logging.error(response.body.decode("utf-8").encode('cp1251'))
        urlname = response.url.replace("/", ".") + '.php'
        urlname = urlname.replace(":", "")
        f = open(urlname, 'w', encoding='utf-8')
        f.write(response.body.decode("utf-8").encode('cp1251').decode('cp1251'))
        if "Goutam" in response.body:
            print("Successfully logged in. Let's start crawling!")
        else:
            print("Login unsuccessful")
        return response.body.decode("cp1251").encode('cp1251')