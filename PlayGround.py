from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.contrib.loader.processor import TakeFirst
from scrapy.contrib.loader import XPathItemLoader
from scrapy.selector import HtmlXPathSelector
from scrapy import FormRequest
from scrapy.item import Item, Field
import scrapy


class PlayGroundItem(Item):
    title = Field()
    url = Field()
    download_url = Field()


class PlayGroundLoader(XPathItemLoader):
    default_output_processor = TakeFirst()


class PlayGroundSpider(scrapy.Spider):
    name = "playground_spider"
    allowed_domains = ["http://www.playground.ru/files/stalker_clear_sky/"]
    # start_urls = ["http://www.playground.ru/files/stalker_clear_sky/"]

    def start_requests(self):
        return [FormRequest("http://www.playground.ru/files/stalker_clear_sky/",
                            formdata={'mode': 'wait', 'download_url': 'http://www.playground.ru/download/?file=147583&mirror=&from=http'},
                            callback=self.parse)]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        l = PlayGroundLoader(PlayGroundItem(), hxs)
        l.add_value('url', response.url)
        l.add_xpath('title', "//div[@class='article-header']/h1/text()")
        l.add_xpath('download_url', "//div[@class='download-links-set']/input[@name='download_url']/@value")
        # if hxs.xpath("//div[@class='download-links-set']/input[@name='download_url']/@value"):
        #     formdata = {
        #         hxs.xpath("//div[@class='download-links-set']/input[@name='mode']/@name"): hxs.xpath("//div[@class='download-links-set']/input[@name='mode']/@value"),
        #         hxs.xpath("//div[@class='download-links-set']/input[@name='download_url']/@name"): hxs.xpath(
        #             "//div[@class='download-links-set']/input[@name='download_url']/@value")
        #     }
        #     yield FormRequest(url=l['download_url'], formdata=formdata, callback=self.parse)
        return l.load_item()