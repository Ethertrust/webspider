from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.contrib.loader.processor import TakeFirst
from scrapy.contrib.loader import XPathItemLoader
from scrapy.selector import HtmlXPathSelector
from scrapy import FormRequest
from scrapy.item import Item, Field


class PlayGroundItem(Item):
    title = Field()
    url = Field()
    download_url = Field()


class PlayGroundLoader(XPathItemLoader):
    default_output_processor = TakeFirst()


class PlayGroundSpider(CrawlSpider):
    name = "playground_spider"
    allowed_domains = ["www.playground.ru"]
    start_urls = ["http://www.playground.ru/files/stalker_clear_sky/"]
    rules = (
        Rule(LinkExtractor(allow=('/files/s_t_a_l_k_e_r_chistoe_nebo')), follow=True, callback='parse_item'),
    )


    def parse_item(self, response):
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