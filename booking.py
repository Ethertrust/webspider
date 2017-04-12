import scrapy
from scrapy.http.request import Request

class QuotesSpider(scrapy.Spider):
    name = "booking"
    start_urls = [
        'https://www.booking.com/hotel/us/the-linq-and-casino.ru.html?aid=360794;label=gog235jc-index-ru-XX-XX-unspec-ru-com-L%3Aru-O%3AwindowsS7-B%3Achrome-N%3AXX-S%3Abo-U%3Aa-H%3As;sid=32f52dc8fef848f088bfdb7e0339d75e;all_sr_blocks=110675811_99136769_0_0_0;checkin=2017-04-15;checkout=2017-04-16;dest_id=20079110;dest_type=city;dist=0;highlighted_blocks=110675811_99136769_0_0_0;hpos=2;room1=A%2CA;sb_price_type=total;srfid=69987ac0ad5590b86624ef023d10077180de78b8X2;type=total;ucfs=1&#hotelTmpl'
    ]

    def make_requests_from_url(self, url):
        return Request(url, dont_filter=True, meta={
            'dont_redirect': True,
            'handle_httpstatus_list': [301, 302]
        })

    def parse(self, response):
        list = []
        for quote in response.css('span'):
            print(quote)
            yield {
                'title': quote.css('span.text::text').extract_first(),
            }

        # next_page = response.css('li.next a::attr(href)').extract_first()
        # if next_page is not None:
        #     next_page = response.urljoin(next_page)
        #     yield scrapy.Request(next_page, callback=self.parse)