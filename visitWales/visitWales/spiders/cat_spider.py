
import scrapy
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

sites = [base+filt for filt in filters]

"""
this spider loops through the category pages, checking which category checkbox is checked 
and extracts the label text to match to the index
"""
class catSpider(scrapy.Spider):
    name = "cat"
    download_delay = 2
    allowed_domains = ["visitwales.com"]
    start_urls = sites
    
    def parse(self, response):
        item = Activity()
        s = response.url
        item['catid'] = s.split('filterIds=')[1]
        item['catname'] = response.xpath("//*[@checked='checked']/../label/text()").extract()
        yield item