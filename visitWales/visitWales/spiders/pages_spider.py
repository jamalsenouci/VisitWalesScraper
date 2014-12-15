
import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
import re
from visitWales.items import Activity

base = "http://www.visitwales.com/activity-search/activity-search-results?\
location=Snowdonia+Mountains+and+Coast&industry=Activities&radius=10&filterIds="
filters = [ 'Index-101321143398%252c',
            'Index-101321143728%252c',
            'Index-101321143513%252c',
            'Index-101321143401%252c',
            'Index-101321143771%252c',
            'Index-101321143392%252c',
            'Index-1013211434034209%252c',
            'Index-101321143402%252c',
            'Index-101321143411%252c',
            'Index-101520163302%252c',
            'Index-101321173346%252c',
            'Index-101520093023%252c',
            'Index-101322143514%252c',
            'Index-101322143512%252c',
            'Index-101322143415%252c',
            'Index-101322143417%252c',
            'Index-101322143518%252c',
            'Index-101322143418%252c',
            'Index-101322143421%252c',
            'Index-101322143420']

filters = [base+filt for filt in filters]
class pagesSpider(CrawlSpider):
    name = "pages"
    download_delay = 2
    allowed_domains = ["visitwales.com"]
    start_urls = filters
    rules = (Rule (LinkExtractor(restrict_xpaths=('//*[@id="next"]',))),
    Rule (LinkExtractor(restrict_xpaths=('//*[@id="mainform"]/div[3]/div/div[1]/article/div/section/ul[2]/li/a[1]',))
    , callback="parse_items"),
    )
    
    def parse_items(self, response):
        item = Activity()
        s = response.url
        start = 'filterIds='
        end = '&'
        item['catid'] = [re.search('%s(.*?)%s' % (start, end), s).group(1)]
        item['name'] = response.xpath('//*[@id="mainform"]/div[3]/div/div[1]/section/h1/text()').extract()
        item['addr'] = response.xpath('//*[@id="mainform"]/div[3]/div/div[1]/section/h3/text()').extract()
        item['tel'] = response.xpath('//*[@id="mainform"]/div[3]/div/div[1]/section/ul/li[1]/span/text()').extract()
        item['site'] = response.xpath('//*[@id="main_0_content_0_WebLink"]/@href').extract()
        item['desc'] = response.xpath('//*[@id="mainform"]/div[3]/div/div[1]/article/div/section/div[1]/p/text()').extract()
        yield item
    