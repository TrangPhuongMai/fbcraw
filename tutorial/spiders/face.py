import scrapy

class face (scrapy.Spider):
    name = "quotes"
    start_urls = [
        'https://www.facebook.com/MTP.Fan/',
        'https://www.facebook.com/tran.thanh.ne/',
        'https://www.facebook.com/hariwonstar/',
        'https://www.facebook.com/xdieunhix/',
        'https://www.facebook.com/BbTranBbbgEntertainment/',
    ]

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)