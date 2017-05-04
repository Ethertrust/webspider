import scrapy
from scrapy.loader.processors import TakeFirst
from scrapy.loader import ItemLoader
from scrapy import FormRequest
from scrapy.item import Item, Field


class PlayGroundItem(Item):
    title = Field()
    url = Field()
    download_url = Field()


class PlayGroundLoader(ItemLoader):
    default_output_processor = TakeFirst()


class PlayGroundSpider(scrapy.Spider):
    name = "playground_spider"
    # allowed_domains = ["http://www.playground.ru/files/stalker_clear_sky/"]
    # start_urls = ["http://www.playground.ru/files/stalker_clear_sky/"]
    start_urls = ['https://auth.playground.info/ru/login']

    def parse(self, response):
        self.logger.info("Starting login procedure!!")
        return FormRequest.from_response(
            response,
            formdata={'_name':'Ethertrust', '_password':'STARWARS1', "_csrf_token":""},
            callback=self.after_login
        )

    def after_login(self, response):
        # check login succeed before going on
        if "Недействительные аутентификационные данные." in response.body:
            self.logger.error("Login failed")
            return
        else:
            self.logger.info("Login succeded")