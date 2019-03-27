import scrapy


class QuotesSpider(scrapy.Spider):
    name = "musicas"
    start_urls = [
        'https://www.letras.mus.br/muse/27396/traducao.html',
        'https://www.letras.mus.br/the-killers/155055/traducao.html',
    ]

    def parse(self, response):
        for quote in response.css('div.cnt-trad_l'):
            yield {
                
                'Original': quote.css('::text').getall(),
                #'Traduzido': quote.css('div.cnt-trad_r.p::text').getall(),
                
            }
        for quote in response.css('div.cnt-trad_r'):
            yield {
                
                #'Original': quote.css('div.cnt-trad_l p::text').getall(),
                'Traduzido': quote.css('::text').getall(),
                
            }