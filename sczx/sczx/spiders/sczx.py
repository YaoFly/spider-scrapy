# encoding=utf-8
import scrapy
from scrapy.http import Request, FormRequest


class QuotesSpider(scrapy.Spider):
    name = "sczx"
    host = "http://www.sczxvip.com/dz/"
    start_urls = [
        host+'list_195_1_m.html'
    ]

    # def start_requests(self):
    #     for i, url in enumerate(self.start_urls):
    #         yield FormRequest(url, meta = {'cookiejar': i},
    #                           headers = self.headers,
    #                           cookies =self.cookies,
    #                           callback = self.parse)


    def parse(self, response):
        links = response.xpath('//div[@class="imgholder"]')
        # item = dict()
        # item['browseurl'] = response.url

        for index, link in enumerate(links):
            detail = link.xpath('a/@href').extract()
            request = scrapy.Request(detail[0], callback=self.detail_parse)
            # request.meta['item'] = item
            yield request
        cnstr = '下一页'
        str = cnstr.decode('utf-8')
        url_next = response.xpath('//a[text()="'+str+'"]/@href').extract()
        print url_next
        if url_next:
            yield scrapy.Request(self.host+url_next[0], callback=self.parse)

    def detail_parse(self, response):
        # item = response.meta['item']
        swfs = response.css('script').re('var flashvars={\r\n                            f:\'(.*?)\',')
        for index, swf in enumerate(swfs):
            yield {
                'swfurl': swf,
                'browseurl': response.url
            }
