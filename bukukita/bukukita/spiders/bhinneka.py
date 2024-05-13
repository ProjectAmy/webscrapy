import scrapy
from ..items import BukukitaItem

class BhinnekaSpider(scrapy.Spider):
    name = "bhinneka"
    allowed_domains = ["bhinneka.com"]
    start_urls = ["https://bhinneka.com/jual-furniture/4lYAjEM"]

    def parse(self, response):

        # Mendapatkan daftar produk dari halaman saat ini
        products = response.css("div.o_wsale_product_grid_wrapper")

        for product in products:
            # Mengekstrak informasi produk seperti nama, harga, dan cicilan
            # nama_product = product.css("h6.o_wsale_products_item_title a::text").get()
            # harga = product.css("span.oe_currency_value::text").get()
            # cicilan = product.css("span.bmd-installment::text").get()

            bukuitem = BukukitaItem()
            bukuitem['nama_product'] = product.css("h6.o_wsale_products_item_title a::text").get()
            bukuitem['harga'] = product.css("span.oe_currency_value::text").get()
            bukuitem['cicilan'] = product.css("span.bmd-installment::text").get()

            # Menghasilkan bukuitem dengan informasi produk yang diekstrak
            # yield {
            #     'nama_product': nama_product,
            #     'harga': harga,
            #     'cicilan': cicilan
            # }
            yield bukuitem

        # Mengambil URL halaman berikutnya menggunakan XPath
        next_page = response.xpath('//*[@id="products_grid"]/div[5]/ul/a/@href').get()

        if next_page is not None:
            # Mengikuti URL halaman berikutnya dan memanggil kembali fungsi parse
            yield response.follow(next_page, callback=self.parse, dont_filter=True)
        else:
            # Jika tidak ada URL halaman berikutnya, mencoba URL alternatif
            next_page = response.xpath('//*[@id="products_grid"]/div[5]/ul/li[7]/a/@href').get()

            if next_page is not None:
                # Mengikuti URL alternatif dan memanggil kembali fungsi parse
                yield response.follow(next_page, callback=self.parse, dont_filter=True)
            else:
                # Jika tidak ada URL halaman berikutnya atau alternatif, mengakhiri scraping
                pass