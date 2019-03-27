import scrapy


class QuotesSpider(scrapy.Spider):
    name = "bandas"
    start_urls = [
        'https://www.letras.mus.br/muse//traducoes.html',
        'https://www.letras.mus.br/the-killers//traducoes.html',
        'https://www.letras.mus.br/queen/traducoes.html',
        'https://www.letras.mus.br/ed-sheeran/traducoes.html',
        'https://www.letras.mus.br/the-beatles/traducoes.html',
        'https://www.letras.mus.br/coldplay/traducoes.html',
        'https://www.letras.mus.br/bruno-mars/traducoes.html',
        'https://www.letras.mus.br/arctic-monkeys/traducoes.html',
        'https://www.letras.mus.br/pearl-jam/traducoes.html',
        'https://www.letras.mus.br/guns-n-roses/traducoes.html',
        'https://www.letras.mus.br/adele/traducoes.html',
        'https://www.letras.mus.br/metallica/traducoes.html',
        'https://www.letras.mus.br/nirvana/traducoes.html',
        'https://www.letras.mus.br/oasis/traducoes.html',
        'https://www.letras.mus.br/keane/traducoes.html',
        'https://www.letras.mus.br/my-chemical-romance/traducoes.html',
        'https://www.letras.mus.br/the-cranberries/traducoes.html',
        'https://www.letras.mus.br/the-smiths/traducoes.html',
        'https://www.letras.mus.br/foo-fighters/traducoes.html',
        'https://www.letras.mus.br/radiohead/traducoes.html',
        'https://www.letras.mus.br/john-lennon/traducoes.html',
        'https://www.letras.mus.br/led-zeppelin/traducoes.html',
        'https://www.letras.mus.br/elton-john/traducoes.html',
        'https://www.letras.mus.br/aerosmith/traducoes.html',
        'https://www.letras.mus.br/panic-at-the-disco/traducoes.html',
        'https://www.letras.mus.br/bon-jovi/traducoes.html',
        
    ]

    def parse(self, response):
        for quote in response.css('ul.cnt-list'):
            yield {
                #'title': quote.css('span.text::text').get(),
                #'href': quote.css('href::text').get(),
                #'sapo': quote.css('a::text').get(),
                #'cavalo': quote.css('.cnt-list li::text').get(),
                'Musicas': quote.css('a::text').getall(),
                #'Links': quote.css('a.href::attr(href)').getall(),
                #'CLinks': quote.css('href.a::attr(href)').getall(),
                'Links': quote.css('a::attr(href)').getall(),
            }
        