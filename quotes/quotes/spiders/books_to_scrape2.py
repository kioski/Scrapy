import scrapy

class BooksSpider(scrapy.Spider):
    name = 'books'
    start_urls = ['http://books.toscrape.com/catalogue/page-%s.html' % page for page in range(1,51)]

    def parse(self, response):
        for book_div in response.css('.row .product_pod'):
            if float(book_div.css('.price_color ::text').get()[1:]) <= float(50):

                yield {
                        'bookName': book_div.css('.thumbnail ::attr(alt)').get(),
                        'starRating' : book_div.css('.star-rating ::attr(class)').get()[12:],
                        'bookPrice in (EUR)' : book_div.css('.price_color ::text').get()[1:],
                        'imageLink' : response.urljoin(book_div.css('.thumbnail ::attr(src)').get())
                    }



