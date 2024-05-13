import scrapy
from ..items import BukukitaItem

class LinkbukuSpider(scrapy.Spider):
    name = "linkbuku"
    allowed_domains = ["www.bukukita.com"]
    start_urls = ["https://www.bukukita.com/katalogbuku.php"]#?page=" + str(i) for i in range(1, 20)]

    def parse(self, response):

        urls = response.css("div.ellipsis a::attr(href)").getall()

        for url in urls:
            if "bukukita.com" not in url:
                url = response.urljoin(url)
            yield scrapy.Request(url, callback=self.find_detail, dont_filter=True)

    def find_detail(self, response):

        buku = BukukitaItem()

        buku['source'] = response.url
        buku['judul'] = response.xpath('//*[@id="pageContent"]/section[2]/div/div/div[1]/div/div[2]/div[5]/div[2]/div[2]/text()').get()
        buku['penulis'] = response.css('a.penulis::text').get()
        buku['penerbit'] = response.css('a.penerbit::text').get()

        yield buku

        # rows = response.css('div.product-info div.row')
        # buku = {'source': response.url}
        # for row in rows:
        #     cols = row.css('div[class*=col] ::text')
        #     if len(cols) == 2:
        #         key = cols[0].get()
        #         value = cols[1].get()
        #         buku.update({key: value})
        # yield buku